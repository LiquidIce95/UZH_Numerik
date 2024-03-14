from unittest import TestCase
import unittest
from week3.ex1_a import evaluationPointsPn

class TestSuite(TestCase):
    
    def test1(self):
        nodalPoints = [1,2]
        f = lambda x : x
        evalPoints = [1,2]
        evalPointsExp = [f(x) for x in evalPoints]
        evalpointsPn = evaluationPointsPn(f,nodalPoints,evalPoints)
        self.assertEqual(evalpointsPn,evalPointsExp)

    def test2(self):
        nodalPoints = [1,2]
        f = lambda x : x**2
        evalPoints = [1,2]
        evalPointsExp = [f(x) for x in evalPoints]
        evalpointsPn = evaluationPointsPn(f,nodalPoints,evalPoints)
        self.assertEqual(evalpointsPn,evalPointsExp)

    def test3(self):
        nodalPoints = [2,3]
        f = lambda x : x**2
        evalPoints = [2,3]
        evalPointsExp = [f(x) for x in evalPoints]
        evalpointsPn = evaluationPointsPn(f,nodalPoints,evalPoints)
        self.assertEqual(evalpointsPn,evalPointsExp)

    def test4(self):
        nodalPoints = [2,3,4]
        f = lambda x : x**2
        evalPoints = [2,3,4]
        evalPointsExp = [f(x) for x in evalPoints]
        evalpointsPn = evaluationPointsPn(f,nodalPoints,evalPoints)
        self.assertEqual(evalpointsPn,evalPointsExp)

    def test5(self):
        nodalPoints = [2,3,4,5,6,7,8]
        f = lambda x : x**2
        evalPoints = [2,3,4,7]
        evalPointsExp = [f(x) for x in evalPoints]
        evalpointsPn = evaluationPointsPn(f,nodalPoints,evalPoints)
        self.assertEqual(evalpointsPn,evalPointsExp)
    

if __name__ == '__main__':
    unittest.main()

