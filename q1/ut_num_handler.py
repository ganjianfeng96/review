import unittest
from num_handler import *

class SzTestCase(unittest.TestCase):
    def setUp(self):
        print "test num_handler start"
    def tearDown(self):
        print "test num_handler stop"
    
    def test_normal_get_num_total(self):
        name = './test.txt'
        self.assertEqual(get_num_total(name),
                         (9, 4247.57))

    def test_abnormal_file_get_num_total(self):
        name = './test1.txt'
        self.assertEqual(get_num_total(name),
                         10.00)


    def test_abnum_file_get_num_total(self):
        name = './test.txt'
        self.assertEqual(get_num_total(name),
                         10.00)
 
if __name__ == "__main__":
    unittest.main()
