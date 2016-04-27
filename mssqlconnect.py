#! /home/songwei/anaconda3/bin/python
# -*- coding: utf-8 -*-

import pymssql
import json
import numpy as np

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
'''
ComsuptionItems = {
    '个护化妆'      :1,
    '服装配饰'      :2,
    '运动户外'      :3,
    '手机/手机配件' :4,
    '珠宝贵金属'    :5,
    '母婴用品'      :6,
    '美食特产'      :7,
    '家具建材'      :8,
    '文化娱乐'      :9,
    '出差旅游'      :10,
    '汽车用品'      :11,
    '医疗保健'      :12,
    '数码'          :13,
    '箱包'          :14,
    '钟表首饰'      :15,
    '日用百货'      :16,
    '鞋'            :17,
    '收藏'      :18,
    '电脑/办公'      :19,
    '家居家纺'      :20,
    '家用电器'      :21,
    '其他'      :22
}

ConsuColum = [[ 'cm_times_top1', 'cm_times_top2', 'cm_times_top3'],
               ['cm_amount_top1', 'cm_amount_top2', 'cm_amount_top3']]

ConsuLevelColum = ['cm_level_top1', 'cm_level_top2', 'cm_level_top3']

MediaColum = ['md_days_top1', 'md_days_top2', 'md_days_top3']

def debugOut(info):
    if (DEBUGOUT == 1):
        print('\n' + info)

def getConsumpItems(itemdict):
    cmitmeslist=[]; cmlables=[];
    for item in itemdict:
        cmlables.append(item)
        cmitem = itemdict[item]
        itemvalues = [int(cmitem.get('number', 0)),
                      int(cmitem.get('pay',0)),
                      int(cmitem.get('visits', 0)),
                      int(cmitem.get('maxpay', 0)) ]
        cmitmeslist.append(itemvalues)
    cmarray = np.array(cmitmeslist)
#    debugOut (cmarray)
    cmindi = np.argsort(-cmarray, axis=0)
#    debugOut ('sorted:')
#    debugOut (cmindi)
#    debugOut(cmlables[cmindi[0][0]])

    colnm = 'cm_cgys, '; values = ''
    i = 0
    for colist in ConsuColum:
        for col in colist:
            colnm = colnm + col + ', '
        for k in range(len(colist)):
            values = values + '\'' + cmlables[cmindi[i][k]] + '\', '
        i += 1
    values = '\'' + ','.join(cmlables) + '\', ' + values
    return colnm, values

def getConsumpLevel(itemdict):
    levelitmeslist=[]; levellables=[]
    for item in itemdict:
        levellables.append(item)
        lvitem = itemdict[item]
        levelitmeslist.append( float(itemdict[item]))
    levelarray = np.array(levelitmeslist)
    lvindi = np.argsort(-levelarray)

    colnm = ''; values = ''
    for i in range(len(levellables)):
        colnm = colnm + ConsuLevelColum[i] + ', '
        values = values + '\'' + levellables[lvindi[i]] + '\', '
    return colnm, values

def procConsumption(consumdict):
    cmitmescol=''
    cmitemval=''
    levelitmescol=''
    levelitemval=''

    if ('month12' in consumdict and consumdict['month12']):
        itemdict = consumdict['month12']
        cmitmescol, cmitemval = getConsumpItems(itemdict)
    elif ('month6' in consumdict and consumdict['month6']):
        itemdict = consumdict['month6']
        cmitmescol, cmitemval = getConsumpItems(itemdict)
    elif ('month3' in consumdict and consumdict['month3']):
        itemdict = consumdict['month3']
        cmitmescol, cmitemval = getConsumpItems(itemdict)
    if  ( 'level' in consumdict and consumdict['level']):
        itemdict = consumdict['level']
        levelitmescol, levelitemval = getConsumpLevel(itemdict)

    return cmitmescol + levelitmescol, cmitemval + levelitemval

def getMediaItems(itemdict):
    mditmeslist = [];
    mdlables = [];
    for item in itemdict:
        mdlables.append(item)
        mditem = itemdict[item]
        itemvalues = int(mditem.get('visitdays', 0))
        mditmeslist.append(itemvalues)
    mdarray = np.array(mditmeslist)
    mdindi = np.argsort(-mdarray)

    colnm = 'md_cgys, ';values = ''
    i = 0
    for colist in MediaColum:
        colnm = colnm + colist + ', '
        values = values + '\'' + mdlables[mdindi[i]] + '\', '
        i += 1
    values = '\'' + ','.join(mdlables) + '\', ' + values
    return colnm, values

def procMedia(mediadict):
    mditmescol=''
    mditemval=''
    if ('month12' in mediadict and mediadict['month12']):
        itemdict = mediadict['month12']
        mditmescol, mditemval = getMediaItems(itemdict)
    elif ('month6' in mediadict and mediadict['month6']):
        itemdict = mediadict['month6']
        mditmescol, mditemval = getMediaItems(itemdict)
    elif ('month3' in mediadict and mediadict['month3']):
        itemdict = mediadict['month3']
        mditmescol, mditemval = getMediaItems(itemdict)
    return mditmescol, mditemval

def getApplyLoanItems(itemdict):
    alitmeslist = [];
    allables = [];
    for item in itemdict:
        mdlables.append(item)
        mditem = itemdict[item]
        itemvalues = int(mditem.get('visitdays', 0))
        mditmeslist.append(itemvalues)
    mdarray = np.array(mditmeslist)
    mdindi = np.argsort(-mdarray)

    colnm = 'md_cgys, ';values = ''
    i = 0
    for colist in MediaColum:
        colnm = colnm + colist + ', '
        values = values + '\'' + mdlables[mdindi[i]] + '\', '
        i += 1
    values = '\'' + ','.join(mdlables) + '\', ' + values
    return colnm, values

def procApplyLoan(apploandiadict):
    mditmescol=''
    mditemval=''
    if ('month12' in apploandiadict):
        itemdict = apploandiadict['month12']
        itmescol, itemval = getApplyLoanItems(itemdict)
    elif ('month6' in apploandiadict):
        itemdict = apploandiadict['month6']
        itmescol, itemval = getApplyLoanItems(itemdict)
    elif ('month3' in apploandiadict):
        itemdict = apploandiadict['month3']
        itmescol, itemval = getApplyLoanItems(itemdict)
    return mditmescol, mditemval


conn = pymssql.connect(host=HOST,port=PORT, user=USER, password=PASSWORD, database=DATABASE, as_dict=True)
cur = conn.cursor()

__comment='''
cur.execute('SELECT ID, CustomerName FROM AnRongCreditReport where ID>100 and ID<200')
for row in cur:
    print ("ID=%d, Name=%s" % (row['ID'], row['CustomerName']) )
'''

#SELECT TOP 30 * FROM ARTICLE WHERE ID NOT IN(SELECT TOP 45000 ID FROM ARTICLE ORDER BY YEAR DESC, ID DESC) ORDER BY YEAR DESC,ID DESC

#cur.execute('Select top 100 * FROM BfdMatchDataV2 where bfd_score = 659 and ID=355239')

i=0
page = 5000
while (True):
    sql = 'Select top %d * FROM BfdMatchDataV2 where ID not in \
              (select top %d ID from BfdMatchDataV2 order by CreatedDate desc, ID desc) order \
              by CreatedDate desc, ID desc'%(page, page * i)
    cur.execute(sql)
    row = cur.fetchone()
    if ( not row ):
        break
    while (True):
        debugOut("ID=%d" % (row['ID']))
        jdict = json.loads(row['JsonData'])
#        columstr = 'INSERT INTO BitLoan_0410.dbo.BfdMatchDataV2 '
        if ('Consumption' in jdict):
                #        debugOut (jdict['Consumption'])
            columstr, valustr = procConsumption(jdict['Consumption'])
            debugOut(columstr + '\n' + valustr)
        if ('Media' in jdict):
                #        debugOut(jdict['Media'])
            columstr, valustr = procMedia(jdict['Media'])
            debugOut(columstr + '\n' + valustr)
#        if ('ApplyLoan' in jdict):
#                #        debugOut(jdict['Media'])
#            columstr, valustr = procApplyLoan(jdict['ApplyLoan'])
#            debugOut(columstr + '\n' + valustr)

        row = cur.fetchone()
        if ( not row ):
            break
    i+=1

__comment='''
while (cur.rowcount > 0 ):
    for row in cur:
        debugOut ("\nID=%d, JsonData=%s" % (row['ID'], row['JsonData']) )
        jdict = json.loads(row['JsonData'])
        columstr = 'INSERT INTO BitLoan_0410.dbo.BfdMatchDataV2 '
        if ( 'Consumption' in jdict):
    #        debugOut (jdict['Consumption'])
            columstr, valustr = procConsumption(jdict['Consumption'])
            debugOut (columstr + '\n' + valustr)
        if ('Media' in jdict):
    #        debugOut(jdict['Media'])
            columstr, valustr = procMedia(jdict['Media'])
            debugOut(columstr + '\n' + valustr)
        if ('ApplyLoan' in jdict):
    #        debugOut(jdict['Media'])
            columstr, valustr = procApplyLoan(jdict['ApplyLoan'])
            debugOut(columstr + '\n' + valustr)
'''
#    print (jdict['Accountchange'])
#    print (jdict['Accountchange']['m1m3'])

#    accountdict = jdict['Accountchange']

#    for accountrow in accountdict:
#        print ( accountrow, accountdict[accountrow] )

conn.close()