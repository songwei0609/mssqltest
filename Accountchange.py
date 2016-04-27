#! /home/songwei/anaconda3/bin/python
# -*- coding: utf-8 -*-

import pymssql
import json
from BfdBase import *

class Accountchange(BfdBase):
    def __init__(self, mejson, insertsql, conn):
        BfdBase.__init__(self)
        self.mejson = mejson
        self.insertsql = insertsql
        self.conn = conn

    def getAccountchangeItems(self, itemdict, mtype):
        __comment='''
            sql = '\ninsert into BfdMatchDataV2Accountchange (CitizenNo, Mobilephone, CreatedDate, UpdatedDate,\
                cardindex, mon_type, cred_cash, cred_default, cred_income, cred_outgo, cred_status,\
                deb_balance, deb_income, deb_outgo, deb_investment, deb_repay, loan) values (%s, %d, %d, \
                %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d)' % \
                  (self.insertsql, cardindex, mtype, \
                   int(credit['cash']), int(credit['default']), int(credit['income']), int(credit['outgo']),
                   int(credit['status']), \
                   int(debit['balance']), int(debit['income']), int(debit['outgo']), int(debit['investment']),
                   int(debit['repay']), int(itemdict['loan']))
        '''

        sql = '\ninsert into BfdMatchDataV2Accountchange (CitizenNo, Mobilephone, CreatedDate, UpdatedDate, mon_type '
        cardindexsql=''
        cardindexval=''
        regionnosql=''
        regionnoval=''
        if ( 'cardindex' in self.mejson and self.mejson['cardindex'] ):
            cardindexsql = ', cardindex'
            cardindexval = ', %d'%int(self.mejson['cardindex'])
        if ( 'regionno' in self.mejson and self.mejson['regionno']):
            regionnosql = ', regionno'
            regionnoval = ', %d'%int(self.mejson['regionno'])

        csql=''
        cval=''
        dsql=''
        dval=''

        if ( 'creditcard' in itemdict and itemdict['creditcard'] ):
            credit = itemdict['creditcard']
            for it in credit:
                if (credit[it]):
                    csql = csql + ', cred_%s'%it
                    cval = cval + ', %d'%int(credit[it])
        if ( 'debitcard' in itemdict and itemdict['debitcard'] ):
            debit = itemdict['debitcard']
            for it in debit:
                if (debit[it]):
                    dsql = dsql + ', deb_%s'%it
                    dval = dval + ', %d'%int(debit[it])

        lsql=') values (%s, %d'%(self.insertsql, mtype)
        lval=')'
        if ( 'loan' in itemdict and itemdict['loan'] ):
            lsql = ', loan' + lsql
            lval = ', %d)'%int(itemdict['loan'])

        sql = sql + cardindexsql + regionnosql + csql + dsql + lsql + cardindexval + regionnoval + cval + dval + lval


#        self.debugOut(sql)
#        curinsert.execute(sql)
#        self.conn.commit()
        return sql

    def procAccountchange(self):
        sql=''
        resql=''
        if ('m1m3' in self.mejson and self.mejson['m1m3']):
            itemdict = self.mejson['m1m3']
            resql = self.getAccountchangeItems(itemdict, 1)
        sql = sql + resql
        resql = ''
        if ('m4m6' in self.mejson and self.mejson['m4m6']):
            itemdict = self.mejson['m4m6']
            resql = self.getAccountchangeItems(itemdict, 2)
        sql = sql + resql
        resql = ''
        if ('m7m9' in self.mejson and self.mejson['m7m9']):
            itemdict = self.mejson['m7m9']
            resql = self.getAccountchangeItems(itemdict, 3)
        sql = sql + resql
        resql = ''
        if ('m10m12' in self.mejson and self.mejson['m10m12']):
            itemdict = self.mejson['m10m12']
            resql = self.getAccountchangeItems(itemdict, 4)
        sql = sql + resql
        resql = ''
        if ('m13m15' in self.mejson and self.mejson['m13m15']):
            itemdict = self.mejson['m13m15']
            resql = self.getAccountchangeItems(itemdict, 5)
        sql = sql + resql
        resql = ''
        if ('m16m18' in self.mejson and self.mejson['m16m18']):
            itemdict = self.mejson['m16m18']
            resql = self.getAccountchangeItems(itemdict, 6)
        sql = sql + resql
        return sql



