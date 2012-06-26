#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Tony.Shao'

import sys
import MySQLdb
import Logger

class Database(object):

    def __init__(self):
        self.db =  MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='dandelion_crawler', charset='utf8')
        self.logger = Logger.getLogger("Database")

    def query(self,sql):
        result = []
        if self.db is None:
            raise DatabaseError("-2", "数据库链接创建异常！")
            self.logger.error("数据库链接失败！")
            return result
        cursor = self.db.cursor(MySQLdb.cursors.DictCursor)
        counts = cursor.execute(sql)
        for row in cursor.fetchall():
            result.append(row)
        self.logger.info("共返回数据 " + counts + " 条")
        cursor.close()
        return result

    def update(self,sql):
        if self.db is None:
            raise DatabaseError("-2", "数据库链接创建异常！")
            self.logger.error("数据库链接失败！")
        cursor = self.db.cursor(MySQLdb.cursors.DictCursor)
        result = cursor.execute(sql)
        cursor.close()
        print result

class DatabaseError(StandardError):
    def __init__(self, error_code, error):
        self.error_code = error_code
        self.error = error
        StandardError.__init__(self, error)

    def __str__(self):
        return 'TokenGeneratorError: ErrorCode: %s, ErrorContent: %s' % (self.error_code, self.error)

if __name__ == '__main__':
    dbUtil = Database()
    dbUtil.query("SELECT * FROM tb_account_info")
#    dbUtil.update("UPDATE tb_account_info SET access_token = '112'")
