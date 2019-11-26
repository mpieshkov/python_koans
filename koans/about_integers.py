#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

__ = False


class AboutIntegers(unittest.TestCase):

    def test_integer_creation(self):

        an_integer = 5

        assert type(an_integer) == int

    def test_integer_constructor_useful_for_converting_from_string(self):

        five = '5'

        assert type(five) != int

        another_five = int('5')

        assert type(another_five) == int

    def test_integer_arithmetic(self):

        assert 1 + 3 == 4
        assert 3 * 3 == 9
        assert 3 ** 2 == 9
        assert 9 / 3 == 3
        assert 6 - 3 == 3

    def test_integers_comparisons(self):

        assert (1 < 3)  == True         # less than
        assert (3 > 3)  == False         # more than
        assert (3 == 2) == False         # equality
        assert (9 <= 3) == False         # less or equal than
        assert (6 >= 3) == True         # more or equal than
