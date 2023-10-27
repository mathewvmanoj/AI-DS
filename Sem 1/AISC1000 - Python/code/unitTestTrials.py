import unittest

def sumUp(a,b):
    return (a+b)

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_sumUp(self):
        self.assertEqual(sumUp(1,2), 3)
