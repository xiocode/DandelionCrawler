#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Tony.Shao'

import sys
import MySQLdb
import Logger

class Database(object):

    def __init__(self):
        self.db =  MySQLdb.connect(host='127.0.0.1', user='root', passwd='299792458', db='dandelion_crawler', charset='utf8')
        self.logger = Logger.getLogger("Database")

    def query(self,sql):
        result = []
        if self.db is None:
            self.logger.error("数据库链接失败！")
            return result
        cursor = self.db.cursor(MySQLdb.cursors.DictCursor)
        counts = cursor.execute(sql)
        for row in cursor.fetchall():
            result.append(row)
        self.logger.info("共返回数据 " + str(counts) + " 条")
        cursor.close()
        return result

    def update(self,sql):
        if self.db is None:
            self.logger.error("数据库链接失败！")
        cursor = self.db.cursor(MySQLdb.cursors.DictCursor)
        result = cursor.execute(sql)
        cursor.close()
        print result

if __name__ == '__main__':
    dbUtil = Database()
    dbUtil.query("SELECT * FROM tb_account_info")
#    dbUtil.update("UPDATE tb_account_info SET access_token = '112'")
