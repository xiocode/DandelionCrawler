#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Tony.Shao'

import sys
import MySQLdb

class Database(object):

    def __init__(self):
        self.db =  MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='dandelion_crawler', charset='utf8')

    def query(self,sql):
        cursor = self.db.cursor(MySQLdb.cursors.DictCursor)
        result = cursor.execute(sql)
        print result
        for row in cursor.fetchall():
            print row
        cursor.close()

    def update(self,sql):
        cursor = self.db.cursor()
        result = cursor.execute(sql)
        print result



if __name__ == '__main__':
    dbUtil = DatabaseUtil()
    dbUtil.query("SELECT * FROM tb_account_info")
#    dbUtil.update("UPDATE tb_account_info SET access_token = '112'")
