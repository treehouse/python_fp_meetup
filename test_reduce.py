import unittest

from functools import reduce

nums = list(range(1, 10))
states = ['Ohio', 'Alaska', 'California', 'Oklahoma']


class TestReduceFunctions(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_nums, sum(nums))

    def test_multiply_numbers(self):
        self.assertEqual(multiply_nums, 362880)

    def test_longest_string(self):
        self.assertEqual(longest_string, 'California')


def add_two_nums(x, y):
    return x + y


def multiply_two_nums(x, y):
    return x * y


def longest(string1, string2):
    if len(string1) > len(string2):
        return string1
    else:
        return string2



if __name__ == '__main__':
    unittest.main()
