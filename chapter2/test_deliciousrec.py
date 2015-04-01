'''
Created on Mar 31, 2015

@author: csu
'''
import unittest
import deliciousrec


class Test(unittest.TestCase):

    def test_initializeUserDict(self):
        results = deliciousrec.initializeUserDict('programming', 5)
        print results


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_initializeUserDict']
    unittest.main()