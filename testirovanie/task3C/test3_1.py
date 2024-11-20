import unittest
from task3 import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
    
    def test_default(self):
        self.assertEqual(self.sol.encrypt('ggg'), '222222')

    def test_for_switch_char(self):
        self.assertEqual(self.sol.encrypt('j'), 'i')

    def test_for_switch_char(self):
        self.assertEqual(self.sol.encrypt('!?'), '!?')

    def test_for_switch_char(self):
        self.assertEqual(self.sol.encrypt('abcdefghijklmnopqrstuvwxyz'), '1112131415212223242431323334354142434445515253545561')

    def test_failed1(self):
        self.assertEqual(self.sol.encrypt('i'), 'j')

if __name__ == '__main__':
    unittest.main()