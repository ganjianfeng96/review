'''
 File Description:
     This file implements: 
     1.log handling function basing on the log level .
     2.log storage and the log name handling

 #Input:
     1.log level:debug/info/warning/error/critical
     2.content to be stored in the log file
 #Output: 
     1.log name in the current procedure path
     2.content was written in the log file

 #Key Points:
  1. Implementation basing on the log level
  2. Log file create and content writing
  
 #Todos:
     1.Log input is variable, such as print, current solution is fixed
     2.Configuration-based development
     3.Log level can be adapted in an intellecture way
  
  # modification history:
  # ----------------------------------------------------
  # 2016/03/19, Jeff Gan, Create
  #
  
  
 '''

import sys
import logging
import time

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}


def writeLog(log_level, message):
    logger=logging.getLogger()
    filename = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

    handler=logging.FileHandler("./"+ filename + ".log")
    
    logger.addHandler(handler)
    if (log_level == 'debug'):
        logger.debug(message)
    elif (log_level == 'info'):
        #logger.debug(message)
        logger.info(message)
    elif (log_level == 'warning'):
        #logger.debug(message)
        #logger.info(message)
        logger.warning(message)
    elif (log_level == 'error'):
        #logger.debug(message)
        #logger.info(message)
        #logger.warning(message)
        logger.error(message)
    elif (log_level == 'critical'):
        #logger.debug(message)
        #logger.info(message)
        #logger.error(message)
        #logger.warning(message)
        logger.critical(message)
    else:
        # in default, only the output is critical
        log_level = critical
        # logger.critical(message)
        logger.error("This is an error input, please choose from: debug/info/warning/error/critial")

    level = LEVELS.get(log_level, logging.NOTSET)
    logging.basicConfig(level=level)
    logger.setLevel(level)
 
