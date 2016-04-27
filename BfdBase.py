#! /home/songwei/anaconda3/bin/python
# -*- coding: utf-8 -*-

import pymssql
import json

class BfdBase:
    def __init__(self):
        self.DEBUG = 1

    def debugOut(self, info):
        if (self.DEBUG == 1):
            print('\n')
            print(info)

