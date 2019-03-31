# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 15:42:54 2019

@author: Xinji
"""
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()

class Solution2(object):
    
    '''
    fail in some case
    '''
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        ans = ''
        for chrt in str:
            if ord(chrt) <=  97 and ord(chrt) >65:
                ans = ans +chr(ord(chrt)+32)
            else: 
                ans =ans + chr(ord(chrt))
        return ans
