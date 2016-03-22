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
	  2.Configuration based developing
  
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
from fibonacci import *
from http_server import *

reload(sys)
sys.setdefaultencoding('utf-8')

def http_app():
    #step 1: get the server name and port 
	#step 2: create the obj of the http_server
	#step 3: run the http server procedure
    app_server = http_server()
    
    app_server.__host = sys.argv[1]
    writeLog('info', app_server.__host)

    #For in the test env, the port can not be configured as expected for the policy, 
	#So we make the port fixed in this feature
	#app_server.__port = int(sys.argv[2])
    #print "the port num is",app_server.__port
    
    app_server.init()
    app_server.run()
    app_server.over()

if __name__ == "__main__" :
    http_app()



