#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        # ここから追加のテストケース
        def test_threshold1 (self):
                self.assertEqual (810, calc(1,810))

        def test_threshold2 (self):
                self.assertEqual (-1, calc(0,810))
        
        def test_threshold3 (self):
                self.assertEqual (809190, calc(999,810))

        def test_threshold4 (self):
                self.assertEqual (-1, calc(1000,810))
        
        def test_threshold5 (self):
                self.assertEqual (810, calc(810,1))

        def test_threshold6 (self):
                self.assertEqual (-1, calc(810,0))
        
        def test_threshold7 (self):
                self.assertEqual (809190, calc(810,999))

        def test_threshold8 (self):
                self.assertEqual (-1, calc(810,1000))

        def test_equivalence1 (self):
                self.assertEqual (58596, calc(114,514))
        
        def test_equivalence2 (self):
                self.assertEqual (-1, calc(114,0))
        
        def test_equivalence3 (self):
                self.assertEqual (-1, calc(114,1000))

        def test_equivalence4 (self):
                self.assertEqual (-1, calc(114,"a"))
        
        def test_equivalence5 (self):
                self.assertEqual (-1, calc(0,514))
        
        def test_equivalence6 (self):
                self.assertEqual (-1, calc(0,-1))

        def test_equivalence7 (self):
                self.assertEqual (-1, calc(0,1000))

        def test_equivalence8 (self):
                self.assertEqual (-1, calc(0,"a"))

        def test_equivalence9 (self):
                self.assertEqual (-1, calc(1000,514))

        def test_equivalence10 (self):
                self.assertEqual (-1, calc(1000,0))

        def test_equivalence11 (self):
                self.assertEqual (-1, calc(1000,1001))

        def test_equivalence12 (self):
                self.assertEqual (-1, calc(1000,0.1))

        def test_equivalence13 (self):
                self.assertEqual (-1, calc(0.1,514))

        def test_equivalence14 (self):
                self.assertEqual (-1, calc(0.1,0))

        def test_equivalence15 (self):
                self.assertEqual (-1, calc(0.1,1000))

        def test_equivalence16 (self):
                self.assertEqual (-1, calc(0.1,"a"))
        