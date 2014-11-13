import datetime
import unittest

import pytz

nums = list(range(1, 20))
timezone_strings = [
    'US/Pacific',
    'US/Eastern',
    'Pacific/Samoa',
    'Pacific/Auckland'
]
format_string = 'Hi, my name is {name} and I love {thing}!'
dicts = [
    {'name': 'Kenneth', 'thing': 'Treehouse'},
    {'name': 'Brick', 'thing': 'lamp'},
    {'name': 'Gollum', 'thing': 'my precious'}
]


class TestMapFunctions(unittest.TestCase):
    def test_double_numbers(self):
        self.assertEqual([x/2 for x in double_nums], nums)

    def test_half_numbers(self):
        self.assertEqual([x*2 for x in half_nums], nums)

    def test_timezones(self):
        self.assertTrue(all([
            isinstance(x, datetime.tzinfo) for x in timezones
        ]))

    def test_num_strings(self):
        self.assertTrue(all([isinstance(x, str) for x in num_strings]))

    def test_format_strings(self):
        for index, statement in enumerate(statements):
            self.assertEqual(statement, format_string.format(**dicts[index]))



if __name__ == '__main__':
    unittest.main()
