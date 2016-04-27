#! /home/songwei/anaconda3/bin/python
# -*- coding: utf-8 -*-

import pymssql
import json
from BfdBase import *

class Media(BfdBase):
    def __init__(self, mejson, insertsql, conn):
        BfdBase.__init__(self)
        self.mejson = mejson
        self.insertsql = insertsql
        self.conn = conn
        self.MediaItems={}
        self.getMediaConfig()

    def getMediaConfig(self):
        cur = self.conn.cursor()
        cur.execute('select Name, Value from BfdMediaCategory order by Value')
        for row in cur:
            self.MediaItems[row['Name']] = row['Value']

    def getMediaItems(self, itemdict, montype):
        curinsert = self.conn.cursor()
        sql = ''
        for item in itemdict:
            cmitem = itemdict[item]
            if (item not in self.MediaItems):
                categ = self.MediaItems['未分类']
            else:
                categ = self.MediaItems[item]
            sql =  sql + '\ninsert into BfdMatchDataV2Media (CitizenNo, Mobilephone, CreatedDate, UpdatedDate,\
                   mon_type, Catygory, visitdays) values (%s, %d, %d, %d)' % (self.insertsql, montype, categ, \
                    int(cmitem.get('visitdays', 0)))
#            self.debugOut(sql)
#            curinsert.execute(sql)
#            self.conn.commit()
        return sql

    def procMedia(self):
        sql=''
        resql=''
        if ('month12' in self.mejson and self.mejson['month12']):
            itemdict = self.mejson['month12']
            resql = self.getMediaItems(itemdict, 3)
        sql = sql + resql
        resql = ''
        if ('month6' in self.mejson and self.mejson['month6']):
            itemdict = self.mejson['month6']
            resql = self.getMediaItems(itemdict, 2)
        sql = sql + resql
        resql = ''
        if ('month3' in self.mejson and self.mejson['month3']):
            itemdict = self.mejson['month3']
            resql = self.getMediaItems(itemdict, 1)
        sql = sql + resql
        return sql


