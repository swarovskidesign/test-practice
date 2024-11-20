from task2_3 import Solution
import unittest

class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()

    def test_multiple_occurrences(self):
        self.assertEqual(self.solution.count_sub_in_sec("aaaaaa", "aa"), 3)

    def test_no_occurrences(self):
        self.assertEqual(self.solution.count_sub_in_sec("abcdef", "gh"), 0)

    def test_single_occurrence(self):
        self.assertEqual(self.solution.count_sub_in_sec("abcdef", "cd"), 1)

    def test_same_string_and_substring(self):
        self.assertEqual(self.solution.count_sub_in_sec("hello", "hello"), 1)

if __name__ == "__main__":
    unittest.main()
