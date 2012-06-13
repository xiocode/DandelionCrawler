#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2012-6-4

@author: Tony.Shao
'''

import logging
from DatabaseWrapper import Database
import Logger

class AutoTokenGenerator(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        self.db = Database()
        self.logger = Logger.getLogger("AutoTokenGenerator")
    
    def generatorToken(self, site_id):
        '''
        Auto Generator a valid token for different site platform.
        '''
        tokens = self.__getValidToken(site_id)
        if tokens != None and  len(tokens) > 0:
            return tokens[0]
        else:
            tokens = self.__generatorValidToken(site_id)
            if tokens != None and  len(tokens) > 0:
                return tokens[0]
            else:
                raise TokenGeneratorError("-1", "没有获取到有效的Token！")
#                self.logger.error("没有获取到有效的Token!")
                return None

    def __getValidToken(self,site_id):
        '''
        get a valid token from database.
        '''
        if self.db is None:
            raise TokenGeneratorError("0", "数据库创建链接失败")
#            self.logger.error("数据库创建链接失败")
            return None
        result = self.db.query("SELECT access_token FROM tb_account_info WHERE platform_id = " + str(site_id) + " AND is_valid=1 AND rate_limited=0 ORDER BY assign_counter ASC " )
        return result

    def __generatorValidToken(self,site_id):
        '''
        update a invalid token
        '''
        if self.db is None:
            raise TokenGeneratorError("0", "数据库创建链接失败")
#            self.logger.error("数据库创建链接失败")
            return None
        result = self.db.query("SELECT uid,username,password FROM tb_account_info WHERE platform_id = " + str(site_id) + " AND is_valid=0  ORDER BY assign_counter ASC")
        tokens=[]
        for account_info in result:
            access_token = WeiboTokenGenerator.loginAndGetToken(account_info["username"],account_info["password"])
            self.db.update("UPDATE access_token = '" + access_token + "' WHERE uid=" + account_info["uid"])
            tokens.append(access_token)
        return tokens

class TokenGeneratorError(StandardError):
    def __init__(self, error_code, error):
        self.error_code = error_code
        self.error = error
        StandardError.__init__(self, error)

    def __str__(self):
        return 'TokenGeneratorError: ErrorCode: %s, ErrorContent: %s' % (self.error_code, self.error)


if __name__ == "__main__":
    tokenGenerator = AutoTokenGenerator()
    token = tokenGenerator.generatorToken(1)
    print token
