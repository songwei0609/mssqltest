#! /home/songwei/anaconda3/bin/python
# -*- coding: utf-8 -*-

import pymssql
import json
from BfdBase import *

class ApplyLoan(BfdBase):
    def __init__(self, mejson, insertsql, conn):
        BfdBase.__init__(self)
        self.mejson = mejson
        self.insertsql = insertsql
        self.conn = conn

    def getAllyLoanItems(self, itemdict, montype):
        curinsert = self.conn.cursor()
        sql = ''
        for item in itemdict:
            cmitem = itemdict[item]
            if (item == 'id'):
                idtype=1
            elif (item == 'cell'):
                idtype=2
            else:
                idtype=9
            for bankitem in cmitem:
                if ( bankitem == 'bank'):
                    banktype = 1
                elif ( bankitem == 'notbank'):
                    banktype = 2
                else:
                    banktype = 9
                sql = sql + '\ninsert into BfdMatchDataV2ApplyLoan (CitizenNo, Mobilephone, CreatedDate, UpdatedDate,\
                       mon_type, id_type, bank_type, selfnumber, allnumber, orgnumber) values (%s, %d, %d, %d, %d, %d, %d)' % \
                      (self.insertsql, montype, idtype, banktype, \
                        int(cmitem.get('selfnumber', 0)), int(cmitem.get('allnumber', 0)), int(cmitem.get('orgnumber', 0)))
#                self.debugOut(sql)
#                curinsert.execute(sql)
#                self.conn.commit()
        return sql

    def procApplyLoan(self):
        sql = ''
        resql = ''
        if ('month12' in self.mejson and self.mejson['month12']):
            itemdict = self.mejson['month12']
            resql = self.getAllyLoanItems(itemdict, 3)
        sql = sql + resql
        resql = ''
        if ('month6' in self.mejson and self.mejson['month6']):
            itemdict = self.mejson['month6']
            resql = self.getAllyLoanItems(itemdict, 2)
        sql = sql + resql
        resql = ''
        if ('month3' in self.mejson and self.mejson['month3']):
            itemdict = self.mejson['month3']
            resql = self.getAllyLoanItems(itemdict, 1)
        sql = sql + resql
        return sql
