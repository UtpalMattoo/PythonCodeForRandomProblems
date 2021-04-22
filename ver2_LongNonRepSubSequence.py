# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 11:41:27 2021

@author: Utpal
"""
# ###########################################  Version 1 #######################################################################

class Solution(object):
    
    def __init__(self, s):
        self.s = s
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = []
        new_lst = []
        for char in self.s:
            found_char, lst = self.found (char, lst)                                                              
            new_lst.append(lst)
        return new_lst
    
    def found (self, char, lst):
        new_lst = []
        found_char = False
        
        if not lst:
            new_lst.append(char)
            return found_char, new_lst
        else: 
            for item in lst:    
              if ((char in item) and (item[-1] != 'X')):
                  found_char = True
                  item = item + 'X'                  
                  new_lst.append(item)
                  if char not in new_lst:
                      new_lst.append(char)
              elif ((char not in item) and (item[-1] != 'X')):
                  new_lst.append(item+char)
                  if char not in new_lst:
                      new_lst.append(char)                  
            return found_char, new_lst 
                
  
# s = "abbbb"
# s = "abbac"
s = "pwwkec"
x = Solution(s)
new_lst = x.lengthOfLongestSubstring(s)
print (new_lst)

max_len = 0
max_item = ""
for elem in new_lst:
    for item in elem:
        if (item[-1] == 'X') and (len(item[-1]) >= max_len):
          new_max = len(elem) -1    
          max_item = item
        else:
          new_max = len(elem)
          max_item = item
          
        if (new_max > max_len):
            max_len = new_max
       
print (max_len)
 
    
# subseq, length = x.lengthOfLongestSubstring(s)
# print (subseq)
# print (length)
    
    
# ###########################################  Version 2 #######################################################################
# Here is a smaller simpler solution that does not use the 'X' marker (in the solution above). The above solution assumes the input string does not contain 'X'.
# The below solution is independent of this.

class Solution(object):
    
    # def __init__(self, s):
    #     self.s = s
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        
        d = defaultdict(lambda: 0)
        lst = []
        new_lst = []
                
        if not (0 <= len(s) <= 50000):
           raise ValueError("Input out of bounds")
        if s == "":
           return 0
            
        for char in s:
            found_char, lst = self.found (char, lst)    
            # print (lst)                                                      
            new_lst.append(lst)
        
        for elem in new_lst:
            for item in elem:
                d[item]  = len(item)    
        
        # print (d.keys())
        # print (d.values())
        
        return max(d.values())
  

    def found (self, char, lst):
        new_lst = []
        found_char = False
        
        if not lst:
            new_lst.append(char)
            return found_char, new_lst
        else: 
            for item in lst:    
               if (char not in item):
                  new_lst.append(item+char)
                  if char not in new_lst:
                      new_lst.append(char)   
               else:
                   new_lst.append(char)                 
            return found_char, new_lst 

s = "pwwkew"
max_len = Solution().lengthOfLongestSubstring(s)
print (max_len)
