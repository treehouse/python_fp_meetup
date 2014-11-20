import random
import unittest

nums = [5, 0, -2, 3.4, 10]
state = 'California'
values = [1, 0, True, False, '', 'hello', []]
strings = [
    "Learn how to create mobile apps for free on @Treehouse!",
    "Treehouse of Horror XXV Ended With A Parade of Simpsons Mashups",
    "Working at @Treehouse is loads of fun.",
    "Treehouse loves you."
]
number_stream = (round(random.random()*100) for _ in range(10000))


def word_list():
    f = open('/usr/share/dict/words')
    for line in f.readlines():
        yield line.strip()
    else:
        f.close()


class TestFilterFunctions(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(all([x >= 0 for x in positive_numbers]))

    def test_non_zero_numbers(self):
        self.assertNotIn(0, non_zero_numbers)

    def test_no_vowels_one_word(self):
        for vowel in 'aeiou':
            self.assertNotIn(vowel, no_vowel_word.lower())

    def test_no_falsey(self):
        self.assertTrue(all(no_falsey))

    def test_only_treehouse(self):
        for statement in only_treehouse:
            self.assertTrue(statement.lower().startswith('treehouse'))

    def test_only_modulo_three(self):
        self.assertTrue(all((num % 3 == 0 for num in modulo_three_nums)))

    def test_only_words_over_10_chars(self):
        self.assertTrue(all(filter(lambda x: len(x) > 9, ten_letter_words)))


def positive(num):
    return num >= 0


def non_zero(num):
    return num != 0


def treehouse(string):
    return string.lower().startswith('treehouse')


def remove_vowels(letter):
    return letter not in 'aeiou'


def recombine(letter_list):
    return ''.join(letter_list)


def modulo_three(num):
    return num % 3 == 0


def ten_letters(word):
    return len(word) > 9


positive_numbers = filter(positive, nums)
non_zero_numbers = filter(non_zero, nums)
no_falsey = filter(None, values)
only_treehouse = filter(treehouse, strings)
no_vowel_word = ''.join(filter(remove_vowels, state.lower()))
modulo_three_nums = filter(modulo_three, number_stream)
ten_letter_words = filter(ten_letters, word_list())


if __name__ == '__main__':
    unittest.main()
