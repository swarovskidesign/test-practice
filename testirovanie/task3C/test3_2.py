import unittest
from task3 import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
    
    def test_default(self):
        self.assertEqual(self.sol.decrypt('222222'), 'ggg')

    def test_for_switch_char(self):
        self.assertEqual(self.sol.decrypt('i'), 'i/j')

    def test_for_switch_char(self):
        self.assertEqual(self.sol.decrypt('!?'), '!?')

    def test_for_switch_char(self):
        self.assertEqual(self.sol.decrypt('1112131415212223242431323334354142434445515253545561'), 'abcdefghi/ji/jklmnopqrstuvwxyz')

    def test_random_char_or_txt(self):
        self.assertEqual(self.sol.decrypt('3424440414521544452404441533'), 'deni/js_dvesti/j_sem')

    def test_failed1(self):
        self.assertEqual(self.sol.decrypt('1415111213'), 'ji/jk')

if __name__ == '__main__':
    unittest.main()