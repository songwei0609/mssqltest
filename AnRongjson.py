#! /home/songwei/anaconda3/bin/python
# -*- coding: utf-8 -*-

import pymssql
import json
import time

DEBUGOUT = 1
HOST = '192.168.1.243'
PORT = '1433'
USER = 'db_bitloan'
PASSWORD = '2016@QQxd'
DATABASE = 'bitloan_0410'

def debugOut(info):
    if (DEBUGOUT == 1):
        print('\n' )
        print (info)

def main():

    conn = pymssql.connect(host=HOST,port=PORT, user=USER, password=PASSWORD, database=DATABASE, as_dict=True)
    cur = conn.cursor()
    conn2 = pymssql.connect(host=HOST,port=PORT, user=USER, password=PASSWORD, database=DATABASE, as_dict=True)

    i = 0
    page = 2000
    debugi = 0
    while (True):
        sql=''
        selectsql = 'Select top %d ID, CustomerName, PaperNumber, CONVERT(CHAR(23), ReportTime, 121) as reptime, WjqCount, JqCount, TotalCount, \
                EwjqCount, EjqCount, EtotalCount, ApplyingCount, ApplyPassedCount, ApplyRejectCount, ApplyTotalCount, \
                QueryCount, NormalCreditDetail, AbnormalCreditDetail, ApplyDetails, QueryDetail, BlackData, \
                CONVERT(CHAR(23), CreatedDate, 121) as created, \
                CONVERT(CHAR(23), UpdatedDate, 121) as updated FROM AnRongCreditReport where ID not in \
                (select top %d ID from AnRongCreditReport order by CreatedDate desc, ID desc) order by CreatedDate desc, ID desc'%(page, page * i)
        cur.execute(selectsql)
        row = cur.fetchone()
        if ( not row ):
#        if (i>debugi):
            break
        while (True):
            debugOut("ID=%d" % (row['ID']))
            insql = 'INSERT INTO AnRongCreditReportDecode (CustomerName, PaperNumber, ReportTime, acc_wjq_num, \
                    acc_jq_num, acc_total, acc_ewjq_num, acc_ejq_num, acc_etotal, apy_doing_num, apy_pass_num, \
                    apy_reject_num, apy_total, apy_query_total, '
            inendsql = 'CreatedDate, UpdatedDate) VALUES(\'%s\', \'%s\', convert(datetime,\'%s\'), %d, %d, %d, %d, %d, \
                        %d, %d, %d, %d, %d, %d, '%(row['CustomerName'], row['PaperNumber'], row['reptime'], row['WjqCount'],
                                                   row['JqCount'], row['TotalCount'], row['EwjqCount'], row['EjqCount'],
                                                   row['EtotalCount'], row['ApplyingCount'], row['ApplyPassedCount'],
                                                   row['ApplyRejectCount'], row['ApplyTotalCount'], row['QueryCount'])
            vsql = ''
            valendql = 'convert(datetime,\'%s\'), convert(datetime,\'%s\') )' % (row['created'], row['updated'])

            if ( row['NormalCreditDetail'] and row['NormalCreditDetail'] != 'null' and row['NormalCreditDetail']!='[]'):
                norm = json.loads(row['NormalCreditDetail'])
                loansum = 0.0
                for item in norm:
                    loansum = loansum + float(item.get('loanMoney', '0.0'))
                insql = insql + 'acc_amount, '
                vsql = vsql + '%f, '%loansum

            if ( row['AbnormalCreditDetail'] and row['AbnormalCreditDetail']!='null' and row['AbnormalCreditDetail']!='[]'):
                abnorm = json.loads(row['AbnormalCreditDetail'])
                loansum = 0.0
                for item in abnorm:
                    loansum = loansum + float(item.get('loanMoney', '0.0'))
                insql = insql + 'acc_eamount, '
                vsql = vsql + '%f, '%loansum

            if (row['ApplyDetails'] and row['ApplyDetails'] != 'null' and row['ApplyDetails'] != '[]'):
                appl = json.loads(row['ApplyDetails'])
                canceln = 0
                for item in appl:
                    if ( 'applyResult' in item and item['applyResult'] and item['applyResult']=='05'):
                        canceln+=1
                insql = insql + 'apy_cancel_num, '
                vsql = vsql + '%d, '%canceln

            if (row['QueryDetail'] and row['QueryDetail'] != 'null' and row['QueryDetail'] != '[]'):
                query = json.loads(row['QueryDetail'])
                agent = 0
                unagent = 0
                for item in query:
                    remark = item.get('remark', 'others')
                    if (remark == '本机构'):
                        agent+=1
                    else:
                        unagent+=1
                insql = insql + 'apy_query_total_bjg, apy_query_total_fbjg, '
                vsql = vsql + '%d, %d, '%(agent, unagent)

            black=[]
            if (row['BlackData'] and row['BlackData'] != 'null' and row['BlackData'] != '[]'):
                black = json.loads(row['BlackData'])
            insql = insql + 'blk_num, '
            vsql = vsql + '%d, '%len(black)

            sql = sql + insql + inendsql + vsql + valendql + '\n'
#            debugOut('insql: ' + insql)

            row = cur.fetchone()
            if ( not row ):
                break
        debugOut(sql)
        conn2.cursor().execute(sql)
        conn2.commit()
        i+=1

    conn.close()
    conn2.close()

if __name__ == '__main__':
    stime =  time.time();
    main()
    etime =  time.time();
    print ('\nExecute %d sec, %d min'%(etime-stime, (etime-stime)/60))