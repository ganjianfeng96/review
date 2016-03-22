#!/usr/bin/python

'''
File Description: 
  This file implements main procedure for the feature.
   
#Input:sys args
#Output: 
    The whole procedure is reasonable and the output qualified the requirement 

#Key Points:
 1. sys parameters handling
 2. The whole main procedure
  
#Todos:
      1.More exceptions considerations
  
# modification history:
# ----------------------------------------------------
# 2016/03/19, Jeff Gan, Create
#
  
'''

import os
import sys
import string
import json
#import re

from log_handler import *
from path_parse import *
from num_handler import *

reload(sys)
sys.setdefaultencoding('utf-8')

def cal_num():
    #step 1: get the file from the path and file name
	#step 2: from the filename, get the num and total num
    num = 0
    num_total = 0
	
    f_names = parse_path(sys.argv[1], sys.argv[2])
    print "the actual file name is:", f_names
    writeLog('info', "the actual file name is:")
    writeLog('info', f_names)

    f_name = f_names[0]
    if f_name.strip()=='':
        writeLog('error', "The file name is not in the path, please double check it")
        print "The file name is not in the path, please double check it"
    else:
        writeLog('info', "begin to calculate the num total")  
        num, num_total = get_num_total(f_name)
        print "The total num is", num, "the total is", num_total	
        writeLog('info', num)
        writeLog('info', num_total)
if __name__ == "__main__" :
    cal_num()



