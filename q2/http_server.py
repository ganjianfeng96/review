
'''
decription:
    This file implements http server content parsing and APIs handling function for the feature.

#Input:server name from the sys parameters
#Output: The related fibonacci result  
#Key Points:
   1. Implement the http server class
   2. Implement the http server APIs
   3. Cal the fibonacci number

#Todos:
   1.generalize the function
   2.Configuration-based development
   3.More APIs implementation	

# modification history:
# ----------------------------------------------------
# 2016/03/19, Jeff Gan, Create
# 
'''

import socket
import signal
import errno
import string
from time import sleep 
import urlparse

from fibonacci import *
from log_handler import *


class http_server:
    __host = ""
    #__host = "127.0.0.1"
    __port = 8010
    __request_url = ""
    __request_context = ""
    __request_header = {}
    __response_header = '''\
HTTP/1.1 200 OK
Context-Type: text/html
Server: Python-slp version 1.0
Context-Length: '''
    __run_flag = True
    __lisfd = None 

    def sig_int_handler(self, signo, frame):
        print 'get signo# ',signo
        writeLog('info', signo)
        self.__run_flag = False
        self.__lisfd.shutdown(socket.SHUT_RD)

    def init_http_request_header(self):
        arrHeader = self.__request_context.split("\n")
        statusLine = arrHeader[0].split(" ")
        h = arrHeader[1:]
        KeyValueHeader = {}
        for i in h:
            kv = i.split(":", 2)
            if len(kv) <= 1 :
                break
            KeyValueHeader[kv[0].lower()] = kv[1].strip()
        KeyValueHeader["url"] = "http://%s%s" % (KeyValueHeader["host"], statusLine[1])
        self.__request_header = KeyValueHeader
        self.__request_url = KeyValueHeader["url"]
    
    def get_query_string(self, index):
        print "index", index,"url is", self.__request_url
        url = self.__request_url
        imsi = urlparse.parse_qs(urlparse.urlparse(url).query)
        ret = imsi.get(index, None) # return ['23']
        if ret != None:
            print 'the result is ', ret[0]
            return ret[0]
        else:
            writeLog('error', 'can not get the url')
            return ""

    def get_response(self):
        header = self.__request_header
        num = self.get_query_string("i")
        context = ""
        if num.isdigit():
            if int(num) == 0:
                str_arr = 'No list for the first 0'
                context = "{\"success\":0,\"data\":%d,\"message\":\"the output list is, (%s)\"}" % (0, str_arr)
            else:
                fab = fibonacci(int(num) - 1)
                len_arr = len(fab)
                #str = 'this is test'
                str_arr = ','.join(str(i) for i in fab)
                context = "{\"success\":0,\"data\":%d,\"message\":\"the first num in the fibonacci is, (%s)\"}" % (int(len_arr), str_arr)
                writeLog('info', str_arr)
                writeLog('info', context)
        else:
            context = "{\"success\":-1,\"data\":%d,\"message\":\"input error, (%s)\"}" % (-1, num)
        #response = "%s %d\n\n%s\n\n" % (header, len(context), context)
        response = "%s" % (context)
        writeLog('info', response)
        return response

    def init(self):
        self.__lisfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.__lisfd.bind((self.__host, self.__port))
        self.__lisfd.listen(2)
        self.__run_flag = True 
        signal.signal(signal.SIGINT, self.sig_int_handler)

    def run(self):
        while self.__run_flag:
            try:
                confd, addr = self. __lisfd.accept()
            except socket.error as e:
                if e.errno == errno.EINTR:
                    print 'get a except EINTR'
                    writeLog('info', e.errno)
                else:
                    raise
                continue

            if self.__run_flag == False:
                break;

            self.__request_context = confd.recv(1024)
            if not self.__request_context:
                break
            self.init_http_request_header()
            confd.send(self.get_response())
            confd.close()

    def over():
        pass


