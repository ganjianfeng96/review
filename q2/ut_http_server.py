import unittest
import urlparse
from http_server import *

class SzTestCase(unittest.TestCase):
    def setUp(self):
        print "test path_parse start"
    def tearDown(self):
        print "test path_parse stop"
    
    def test_normal_get_query_string(self):
        self.ut_http = http_server()

        self.ut_http._http_server__request_url = "http://cp01-rdqa-dev390.cp01.baidu.com:8010/?i=3"
        index = "i"
		
        self.assertEqual(3, int(self.ut_http.get_query_string(index)))

    def test_abnormal_get_query_string(self): 
        ut_http = http_server()
        ut_http._http_server__request_url = "http://cp01-rdqa-dev390.cp01.baidu.com:8010/?i=3"
        index = "i"

        self.assertEqual(0, int(ut_http.get_query_string(index)))

if __name__ == "__main__":
    unittest.main()
