#! /home/songwei/anaconda3/bin/python
# -*- coding: utf-8 -*-

import pymssql
import json
import time
import numpy as np
from BfdRecorddecode import *
from Consumption import *
from Media import *
from ApplyLoan import *
from Accountchange import *
from Location import *

DEBUGOUT = 1
HOST = '192.168.1.243'
PORT = '1433'
USER = 'db_bitloan'
PASSWORD = '2016@QQxd'
DATABASE = 'bitloan_0410'

__commet='''
ConsuColum = {
    '服装配饰'  :   'consum_cloth_',
    '珠宝贵金属':   'consum_jew_'
}
ConsuColum = [[ 'cm_times_top1', 'cm_times_top2', 'cm_times_top3'],
               ['cm_amount_top1', 'cm_amount_top2', 'cm_amount_top3']]

ConsuLevelColum = ['cm_level_top1', 'cm_level_top2', 'cm_level_top3']

MediaColum = ['md_days_top1', 'md_days_top2', 'md_days_top3']
'''

DealedKey = ['Flag', 'SpecialList_c', 'ApplyLoan', 'Location', 'LoanEquipment', 'Authentication',\
             'code', 'swift_number', 'Consumption', 'Assets', 'Title', 'Brand', 'Media', \
             'Stability_c', 'Accountchange', 'Rating', \
             'Score', 'Rule']

Novalid = ['DataCust', 'PayConsumption', 'AirTravel', 'TelecomCheck' ]

def debugOut(info):
    if (DEBUGOUT == 1):
        print('\n' + info)

def main():
    stastic = {}
    newkey = {}
    spec_list=[0]
    loeq_list=[0]
    rule_list=[0]
    rulerel_list=[0]
    online_list = [0]
    int_list = [0]
    acc_list = [0]


    spe_list = [0]
    spec_list = [0]
    sta_list = [0]
    stac_list = [0]

    conn = pymssql.connect(host=HOST,port=PORT, user=USER, password=PASSWORD, database=DATABASE, as_dict=True)
    cur = conn.cursor()
    conn2 = pymssql.connect(host=HOST,port=PORT, user=USER, password=PASSWORD, database=DATABASE, as_dict=True)

    i = 6900
    page = 50
    debugi = 0
    while (True):
        insql=''
        selectsql = 'Select top %d ID, CitizenNo, Mobilephone, ApiFlag, BfdAudit, FailedStatus, JsonData, WashStatus, bfd_both_match, \
               bfd_id_match, bfd_cell_match, bfd_score, bfd_final, CONVERT(CHAR(23), CreatedDate, 121) as created, \
               CONVERT(CHAR(23), UpdatedDate, 121) as updated FROM BfdMatchDataV2 where ID not in \
              (select top %d ID from BfdMatchDataV2 order by CreatedDate desc, ID desc) order by CreatedDate desc, ID desc'%(page, page * i)
        cur.execute(selectsql)
        row = cur.fetchone()
        if ( not row ):
#        if (i>debugi):
            break
        while (True):
            debugOut("ID=%d" % (row['ID']))
            sql = ''
            if ( row['JsonData'] ):
                resql=''
                jdict = json.loads(row['JsonData'])
                insertsql = ('\'%s\', \'%s\', convert(datetime,\'%s\'), convert(datetime,\'%s\')' %
                             (row['CitizenNo'], row['Mobilephone'],
                              row['created'], row['updated']))

                bfdrec = BfdRecorddecode(row, conn2)
                resql = bfdrec.decode()
                sql = sql + resql
                resql = ''

                if ('Consumption' in jdict and jdict['Consumption']):
                    consum = Consumption((jdict['Consumption']), insertsql, conn2)
                    resql = consum.procConsumption()
                sql = sql + resql
                resql = ''

                if ('Media' in jdict and jdict['Media']):
                    media = Media((jdict['Media']), insertsql, conn2)
                    resql = media.procMedia()
                sql = sql + resql
                resql = ''

                if ('ApplyLoan' in jdict and jdict['ApplyLoan']):
                    applyloan = ApplyLoan((jdict['ApplyLoan']), insertsql, conn2)
                    resql = applyloan.procApplyLoan()
                sql = sql + resql
                resql = ''

                if ('Accountchange' in jdict and jdict['Accountchange']):
                    accountchange = Accountchange((jdict['Accountchange']), insertsql, conn2)
                    resql = accountchange.procAccountchange()
                sql = sql + resql
                resql = ''

                if ('Location' in jdict and jdict['Location']):
                    applyloan = Location((jdict['Location']), insertsql, conn2)
                    resql = applyloan.procLocation()
                sql = sql + resql

                #dor some check
                for key in jdict:
                    if ( key not in DealedKey ):
                        if ( row['ID'] > newkey.get(key, 0) ):
                            newkey[key] = row['ID']
                    stastic[key] = stastic.get(key, 0) + 1

                if ('LoanEquipment' in jdict and jdict['LoanEquipment']):
                    if (row['ID'] > loeq_list[0]):
                        loeq_list[0] = row['ID']
                if ('Online' in jdict and jdict['Online']):
                    if (row['ID'] > online_list[0]):
                        online_list[0] = row['ID']
                if ('Internet' in jdict and jdict['Internet']):
                    if (row['ID'] > int_list[0]):
                        int_list[0] = row['ID']
                if ('Rule' in jdict and jdict['Rule']):
                    if (row['ID'] > rule_list[0]):
                        rule_list[0] = row['ID']
                if ('RuleResult' in jdict and jdict['RuleResult']):
                    if (row['ID'] > rulerel_list[0]):
                        rulerel_list[0] = row['ID']

#            debugOut('sql: ' + sql)
            insql = insql + sql
#            debugOut('insql: ' + insql)

            row = cur.fetchone()
            if ( not row ):
                break
        debugOut(insql)
        conn2.cursor().execute(insql)
        conn2.commit()
        i+=1

    __comment='''
    print ('\n--------statis--------------')
    for it in stastic:
        print( it, ': ', stastic[it])

    print ('\n loeq_list: ', loeq_list)
    print ('\n int_list: ', int_list)
    print ('\n online_list', online_list)

    print ('\n rule_list', rule_list)
    print('\n rulerel_list', rulerel_list)
    '''
    print ('\n=========new key===========')
    for it in newkey:
        print(it, ': ', newkey[it])

    conn.close()
    conn2.close()

if __name__ == '__main__':
    stime =  time.time();
    main()
    etime =  time.time();
    print ('\nExecute %d sec, %d min'%(etime-stime, (etime-stime)/60))