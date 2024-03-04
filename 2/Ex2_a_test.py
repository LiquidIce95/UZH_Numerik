from unittest import TestCase
import unittest
from Ex2_a import neville


class TestSuite(TestCase):
    
    def test1(self):
        x = [1,2,3,4]
        y = [a for a in x]

        xx = 1
        self.assertEqual(neville(x,y,xx),xx)

    def test2(self):
        x = [1,2,3,4]
        y = [a for a in x]

        xx = 2
        self.assertEqual(neville(x,y,xx),xx)
    
    def test3(self):
        x = [1,2,3,4]
        y = [a for a in x]

        xx = 3
        self.assertEqual(neville(x,y,xx),3)

    def test4(self):
        x = [1,2,3,4]
        y = [a for a in x]

        xx = 4
        self.assertEqual(neville(x,y,xx),xx)

if __name__ == '__main__':
    unittest.main()

