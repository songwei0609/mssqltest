#! /home/songwei/anaconda3/bin/python
# -*- coding: utf-8 -*-

import pymssql
import json
from BfdBase import *
__comment='''
CREATE TABLE BitLoan_0410.dbo.BfdMatchDataV2Consumption (
	ID bigint NOT NULL,
	CitizenNo nvarchar(50) NOT NULL,
	Mobilephone nvarchar(50) NOT NULL,
	Catygory smallint not NULL,
	visits int NOT NULL,
	number int NOT NULL,
	pay int NOT NULL,
	maxpay int NOT NULL,
	CreatedDate datetime NOT NULL,
	UpdatedDate datetime NOT NULL,
	CONSTRAINT PK_BfdMatchDataV2Consumption PRIMARY KEY (ID)
);
'''

class Consumption(BfdBase):
    def __init__(self, cmjson, insertsql, conn):
        BfdBase.__init__(self)
        self.cmjson = cmjson
        self.insertsql = insertsql
        self.conn = conn
        self.ComsuptionItems={}
        self.getComsuptionConfig()

    def getComsuptionConfig(self):
        cur = self.conn.cursor()
        cur.execute('select Name, Value from BfdConsumptionCategory order by Value')
        for row in cur:
            self.ComsuptionItems[row['Name']] = row['Value']

    def getConsumpItems(self, itemdict, montype):
        curinsert = self.conn.cursor()
        sql = ''
        for item in itemdict:
            cmitem = itemdict[item]
            if ( item not in self.ComsuptionItems ):
                categ = self.ComsuptionItems['未分类']
            else:
                categ = self.ComsuptionItems[item]
            sql = sql + '\ninsert into BfdMatchDataV2Consumption (CitizenNo, Mobilephone, CreatedDate, UpdatedDate,\
                   Category, mon_type,visits, number, pay, maxpay) values (%s, %d, %d, %d, %d, %d, %d)'%(self.insertsql, categ, \
                    montype, int(cmitem.get('visits', 0)), int(cmitem.get('number', 0)),\
                    int(cmitem.get('pay', 0)), int(cmitem.get('maxpay', 0)))
#            self.debugOut(sql)
#            curinsert.execute(sql)
#            self.conn.commit()
        return sql

    def getConsumpLevel(self, itemdict):
        curinsert = self.conn.cursor()
        sql=''
        for item in itemdict:
            sql = sql + '\ninsert into BfdMatchDataV2ConsumptionLevel (CitizenNo, Mobilephone, CreatedDate, UpdatedDate,\
                   Catygory, level ) values (%s, %d, %f)'%(self.insertsql, self.ComsuptionItems[item], float(itemdict[item]))
#            self.debugOut(sql)
#            curinsert.execute(sql)
#            self.conn.commit()
        return sql

    def procConsumption(self):
        sql=''
        resql=''
        if ('month12' in self.cmjson and self.cmjson['month12']):
            itemdict = self.cmjson['month12']
            resql = resql + self.getConsumpItems(itemdict,3)
        sql = sql + resql
        resql=''
        if ('month6' in self.cmjson and self.cmjson['month6']):
            itemdict = self.cmjson['month6']
            resql = resql + self.getConsumpItems(itemdict,2)
        sql = sql + resql
        resql=''
        if ('month3' in self.cmjson and self.cmjson['month3']):
            itemdict = self.cmjson['month3']
            resql = resql + self.getConsumpItems(itemdict,1)
        sql = sql + resql
        resql=''
        if  ( 'level' in self.cmjson and self.cmjson['level']):
            itemdict = self.cmjson['level']
            resql = resql + self.getConsumpLevel(itemdict)

        return sql + resql
