import unittest
from fibonacci import *

class SzTestCase(unittest.TestCase):
    def setUp(self):
        print "test path_parse start"
    def tearDown(self):
        print "test path_parse stop"
    
    def test_fibonacci_0(self):
        #self.assertTrue('./test.txt', parse_path(path, name))
		self.assertEqual([0], fibonacci(0))

    def test_fibonacci_1(self):
        self.assertEqual([0,1], fibonacci(1))

    def test_fibonacci_2(self):
        self.assertEqual([0,1,1], fibonacci(2))

    def test_fibonacci_3(self):
        self.assertEqual([0,1,1,2],fibonacci(3))


    def test_fibonacci_5(self):
        self.assertEqual([0,1,1,2,3,5], fibonacci(5))


    def test_abnormal_fibonacci(self):
        self.assertEqual([0], fibonacci(-1))
 
if __name__ == "__main__":
    unittest.main()
