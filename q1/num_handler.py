'''
File Description:
	This file implements file content parsing and handling function for the feature.

#Input:File name and the path of the file
#Output: The assigned type num and the total value of all numbers  
#Key Points:
   1. Get content in the file line by line
   2. Get all the numbers in the RegExp
   3. Cal the total value of all numbers

#Todos:
   1.generalize the function
   2.Configuration-based development

# modification history:
# ----------------------------------------------------
# 2016/03/19, Jeff Gan, Create
# 


'''

import re
import sys

from log_handler import *

def get_num_total(name):
    fp = open(name, 'r')
    num = 0
    num_total = 0
    
    while 1:
        s = fp.readline()
        if not s:
            break
        writeLog('info', s)
    
	    #get all the number including float and int
        aList = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s)
        #print(aList)
    
        for ss in aList:
            print(ss[0]+ss[2])
            writeLog('info', (ss[0]+ss[2]))
            aNum = float((ss[0]+ss[2]))
            num += 1
            print "the num No is: ", num, "and the num value is ",aNum
            writeLog('info', num)
            writeLog('info', aNum)
            
            num_total = num_total + aNum
            print " the total num is: ",num_total
            writeLog('info', num_total)

    print "The total num is", num, "the total of all nums", num_total
    #writeLog('info',  num)
    
    fp.close()
    return num, num_total
#get_num_total(sys.argv[1])
