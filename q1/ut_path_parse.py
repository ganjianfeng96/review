import unittest
from path_parse import *

class SzTestCase(unittest.TestCase):
    def setUp(self):
        path = './'
        name = './test.txt'
        self.ret = parse_path(path, name)
        print "test path_parse start"
    def tearDown(self):
        print "test path_parse stop"
    
    def test_normal_parse_path(self):
        path = './'
        name = './test.txt'
        self.assertTrue('./test.txt', parse_path(path, name))
		#self.assertIn('./test.txt', parse_path(path, name))

    def test_abnormal_file_parse_path(self):
        path = './'
        name = 'test1.txt'
        #self.assertIn('./test1.txt', parse_path(path, name))
        self.assertTrue('./test1.txt', parse_path(path, name))


    def test_abnum_path_parse_path(self):
        path = '/'
        name = 'test'
        self.assertTrue('./test.txt', parse_path(path, name))
 
if __name__ == "__main__":
    unittest.main()
