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


def doubler(num):
    return num * 2


def halver(num):
    return num / 2


def timezone_maker(timezone_string):
    return pytz.timezone(timezone_string)


def string_formatter(values):
    return format_string.format(**values)


double_nums = map(doubler, nums)
half_nums = map(halver, nums)
timezones = map(timezone_maker, timezone_strings)
num_strings = map(str, nums)
statements = map(string_formatter, dicts)

if __name__ == '__main__':
    unittest.main()
