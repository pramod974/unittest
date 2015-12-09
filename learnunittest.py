__author__ = 'Pramod.Kumar'

import unittest
import pandas
#pandas is not lovely !
# Here's our "unit".
def justgit():
    print "git !!!"
def IsOdd(n):
    return n % 2 == 1

# Here's our "unit tests".
class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.failUnless(IsOdd(1))

    def testTwo(self):
        self.failIf(IsOdd(2))

def main():
    unittest.main()

if __name__ == '__main__':
    main()

