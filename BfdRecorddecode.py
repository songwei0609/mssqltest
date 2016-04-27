#! /home/songwei/anaconda3/bin/python
# -*- coding: utf-8 -*-

import pymssql
import json
from BfdBase import *

class BfdRecorddecode(BfdBase):
    def __init__(self, row, conn):
        BfdBase.__init__(self)
        self.row = row
        self.conn = conn
        self.jdict = json.loads(row['JsonData'])
#        self.debugOut(self.jdict)


    def procSubjson(self, subkey):
        rsql=''
        vsql=''
#        self.debugOut(subkey)
        sdict = self.jdict[subkey]

#        self.debugOut(sdict)
        for key in sdict:
            if (sdict[key]):
                rsql = rsql + '%s, '%(key)
                vsql = vsql + '%d, '%int(sdict[key])
        return rsql, vsql

    def procRating(self, subkey):
        rsql=''
        vsql=''
        sdict = self.jdict[subkey]

        for key in sdict:
            if (sdict[key]):
                rsql = rsql + '%s, '%(key)
                vsql = vsql + '\'%s\', '%(sdict[key])
        return rsql, vsql

    def procAuthentication(self, sdict):
        rsql=''
        vsql=''
#        self.debugOut(sdict)
        for key in sdict:
            if ( key == 'id-name' and sdict[key]):
                rsql = rsql + 'auth_id_name, '
                vsql = vsql + '%d, '%int(sdict[key])
            elif (sdict[key]):
                rsql = rsql + 'auth_%s, '%(key)
                vsql = vsql + '%d, '%int(sdict[key])

        return rsql, vsql

    def procStability(self, sdict):
        rsql = ''
        vsql = ''
#        self.debugOut(sdict)
        for key in sdict:
            if (sdict[key]):
                if ( key == 'cell' ):
                    if (sdict['cell']['number']):
                        rsql = rsql + 'st_cell_number, '
                        vsql = vsql + '%d, '%int(sdict[key]['number'])
                    if (sdict['cell']['firsttime']):
                        rsql = rsql + 'st_cell_firsttime, '
                        vsql = vsql + '\'%s\', '%str(sdict[key]['firsttime'])
                elif (sdict[key]['number']):
                    rsql = rsql + 'st_%s, '%(key)
                    vsql = vsql + '%d, '%int(sdict[key]['number'])
        return rsql, vsql

    def procStability_c(self, sdict):
        rsql = ''
        vsql = ''
        rasql=''
        ravsql=''

#        self.debugOut(sdict)
        for key in sdict:
            if ( key == 'Authentication' and sdict['Authentication']):
                rasql, ravsql = self.procAuthentication(sdict['Authentication'])
                rsql = rsql + rasql
                vsql = vsql + ravsql
            elif (sdict[key]):
                if ( key == 'cell' ):
                    if (sdict['cell']['number']):
                        rsql = rsql + 'st_cell_number, '
                        vsql = vsql + '%d, '%int(sdict[key]['number'])
                    if (sdict['cell']['firsttime']):
                        rsql = rsql + 'st_cell_firsttime, '
                        vsql = vsql + '\'%s\', '%str(sdict[key]['firsttime'])
                elif ( sdict[key]['number'] ):
                    rsql = rsql + 'st_%s, '%(key)
                    vsql = vsql + '%d, '%int(sdict[key]['number'])
        return rsql, vsql

    def decode(self):
        row = self.row
        jdict = self.jdict
        startsql = '\ninsert into BfdMatchDataV2Decode (CitizenNo, Mobilephone, ApiFlag, BfdAudit, \
                     FailedStatus, bfd_both_match, bfd_id_match, bfd_cell_match, bfd_score, bfd_final, '
        endsql = 'CreatedDate, UpdatedDate) values ('

        valstartsql = ('\'%s\', \'%s\', %d, %d, %d, %d, %d, %d, %d, \'%s\', '%
                         (row['CitizenNo'], row['Mobilephone'], row['ApiFlag'], row['BfdAudit'], row['FailedStatus'],
                          row['bfd_both_match'], row['bfd_id_match'], row['bfd_cell_match'], row['bfd_score'],
                          row['bfd_final']) )
        valendsql = 'convert(datetime,\'%s\'), convert(datetime,\'%s\') )'%(row['created'], row['updated'])

        sql = ''
        valsql = ''
        resql = ''
        revsql = ''

        if ( 'code' in jdict and jdict['code'] ):
            sql = sql + 'code, '
            valsql = valsql + '%d, '%int(jdict['code'])

        if ('swift_number' in jdict and jdict['swift_number']):
            sql = sql + 'swift_number, '
            valsql = valsql + '\'%s\', ' %jdict['swift_number']

        if ( 'Title' in jdict and jdict['Title'] ):
            resql, revsql = self.procSubjson('Title')
            sql = sql + resql
            valsql = valsql + revsql

        if ( 'Score' in jdict and jdict['Score'] ):
            resql, revsql = self.procSubjson('Score')
            sql = sql + resql
            valsql = valsql + revsql

        if ( 'Assets' in jdict and jdict['Assets'] ):
            resql, revsql = self.procSubjson('Assets')
            sql = sql + resql
            valsql = valsql + revsql

        if ( 'Rating' in jdict and jdict['Rating'] ):
            resql, revsql = self.procRating('Rating')
            sql = sql + resql
            valsql = valsql + revsql

        if ('Authentication' in jdict and jdict['Authentication']):
            resql, revsql = self.procAuthentication(jdict['Authentication'])
            sql = sql + resql
            valsql = valsql + revsql

        if ( 'Stability' in jdict and jdict['Stability']):
            resql, revsql = self.procStability(jdict['Stability'])
            sql = sql + resql
            valsql = valsql + revsql
        elif( 'Stability_c' in jdict and jdict['Stability_c']):
            resql, revsql = self.procStability_c(jdict['Stability_c'])
            sql = sql + resql
            valsql = valsql + revsql

        #   pass


        insql = startsql + sql + endsql + valstartsql + valsql + valendsql

#        self.debugOut(insql)
        return insql




