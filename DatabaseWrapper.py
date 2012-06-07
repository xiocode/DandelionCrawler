#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Tony.Shao'

import sys
import MySQLdb

class Database(object):

    def __init__(self):
        self.db =  MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='dandelion_crawler', charset='utf8')
        self.cursor = self.db.cursor(MySQLdb.cursors.DictCursor)

    def query(self,sql):
        self.cursor.execute(sql)
        result = []
        for row in self.cursor.fetchall():
            result.append(row)
        return result

    def update(self,sql):
        cursor = self.db.cursor()
        result = cursor.execute(sql)
        print result

    def close(self):
        self.cursor.close()

if __name__ == '__main__':
    dbUtil = Database()
    dbUtil.query("SELECT * FROM tb_account_info")
#    dbUtil.update("UPDATE tb_account_info SET access_token = '112'")
