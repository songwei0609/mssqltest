#! /home/songwei/anaconda3/bin/python
# -*- coding: utf-8 -*-

import pymssql
import json
from BfdBase import *

class Location(BfdBase):
    def __init__(self, mejson, insertsql, conn):
        BfdBase.__init__(self)
        self.mejson = mejson
        self.insertsql = insertsql
        self.conn = conn

    def getLocationItems(self, itemdict, atype):
        curinsert = self.conn.cursor()

        ssql = '\ninsert into BfdMatchDataV2Location (CitizenNo, Mobilephone, CreatedDate, UpdatedDate, '
        esql = ' location_type) values ( %s, '%(self.insertsql)
        eval = ' %d)'%atype
        insql = ''
        inval = ''
        for item in itemdict:
            addr = item[-1]
            insql = insql + 'addr' + addr + ', '
            inval = inval + '%f, '%float(itemdict[item])

        sql = ssql + insql + esql + inval + eval
#        self.debugOut(sql)
#        curinsert.execute(sql)
#        self.conn.commit()
        return sql

    def procLocation(self):
        sql=''
        resql=''
        if ('home_addr' in self.mejson and self.mejson['home_addr']):
            itemdict = self.mejson['home_addr']
            resql =self.getLocationItems(itemdict, 1)
        sql = sql + resql
        resql = ''
        if ('biz_addr' in self.mejson and self.mejson['biz_addr']):
            itemdict = self.mejson['biz_addr']
            resql =self.getLocationItems(itemdict, 2)
        sql = sql + resql
        resql = ''
        if ('per_addr' in self.mejson and self.mejson['per_addr']):
            itemdict = self.mejson['per_addr']
            resql =self.getLocationItems(itemdict, 3)
        sql = sql + resql
        resql = ''
        if ('apply_addr' in self.mejson and self.mejson['apply_addr']):
            itemdict = self.mejson['apply_addr']
            resql =self.getLocationItems(itemdict, 4)
        sql = sql + resql
        resql = ''
        if ('oth_addr' in self.mejson and self.mejson['oth_addr']):
            itemdict = self.mejson['oth_addr']
            resql =self.getLocationItems(itemdict, 5)
        sql = sql + resql

        return sql



