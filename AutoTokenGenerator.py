#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2012-6-4

@author: windows
'''

import logging
from DatabaseWrapper import Database
import WeiboTokenGenerator

class AutoTokenGenerator(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        self.db = Database()
    
    def generatorToken(self, site_id):
        '''
        Auto Generator a valid token for different site platform.
        '''
        tokens = self.__getValidToken(site_id)
        if len(tokens) > 0:
            return tokens[0]
        else:
            tokens = __generatorValidToken(site_id)
            if len(tokens) > 0:
                return tokens[0]

    def __getValidToken(self,site_id):
        '''
        get a valid token from database.
        '''
        result = self.db.query("SELECT access_token FROM tb_account_info WHERE platform_id = " + str(site_id) + " AND is_valid=1 AND rate_limited=0 ORDER BY assign_counter ASC " )
        return result

    def __generatorValidToken(self,site_id):
        '''
        update a invalid token
        '''
        result = self.db.query("SELECT uid,username,password FROM tb_account_info WHERE platform_id = " + str(site_id) + " AND is_valid=0  ORDER BY assign_counter ASC")
        tokens=[]
        for account_info in result:
            access_token = WeiboTokenGenerator.loginAndGetToken(account_info["username"],account_info["password"])
            self.db.update("UPDATE access_token = '" + access_token + "' WHERE uid=" + account_info["uid"])
            tokens.append(access_token)
        return tokens



if __name__ == "__main__":
    tokenGenerator = AutoTokenGenerator()
    tokenGenerator.generatorToken(1)
