'''
File Description:
     This file implements file path parsing and handling function.
   
#Input:
    1.File name 
    2.The path of the file
#Output: 
    1. The actual file name and its path
#Key Points:
 1. Parse the path and file name
  
 #Todos:
 1.Configuration-based development
  
 # modification history:
 # ----------------------------------------------------
 # 2016/03/19, Jeff Gan, Create
 # 
  
 '''

import os
import sys

def parse_path(path, name):
    ret = []
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp) and name in filename:
            ret.append(fp)
        elif os.path.isdir(fp):
            ret += parse_path(fp, name)
	
    return ret

