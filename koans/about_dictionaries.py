#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

__ = None


class AboutDictionaries(unittest.TestCase):

    def test_creating_dictionaries(self):

        empty_dict = dict()

        assert dict == type(empty_dict)
        assert {} == empty_dict
        assert 0 == len(empty_dict)

    def test_dictionary_literals(self):

        empty_dict = {}

        assert dict == type(empty_dict)

        babel_fish = {'one': 'uno', 'two': 'dos'}

        assert 2 == len(babel_fish)

    def test_accessing_dictionaries(self):

        babel_fish = {'one': 'uno', 'two': 'dos'}

        assert 'uno' == babel_fish['one']
        assert 'dos' == babel_fish['two']

    def test_changing_dictionaries(self):

        babel_fish = {'one': 'uno', 'two': 'dos'}
        babel_fish['one'] = 'eins'

        expected = {'two': 'dos', 'one': 'eins'}
        assert expected == babel_fish

    def test_dictionary_is_unordered(self):

        dict1 = {'one': 'uno', 'two': 'dos'}
        dict2 = {'two': 'dos', 'one': 'uno'}

        assert ({'one': 'uno', 'two': 'dos'} == {'two': 'dos', 'one': 'uno'}) == (dict1 == dict2)

    def test_dictionary_keys_and_values(self):

        babel_fish = {'one': 'uno', 'two': 'dos'}

        # testing lengths
        assert 2 == len(babel_fish.keys())
        assert 2 == len(babel_fish.values())

        # testing membership
        assert True == ('one' in babel_fish.keys())
        assert False == ('two' in babel_fish.values())
        assert False == ('uno' in babel_fish.keys())
        assert True == ('dos' in babel_fish.values())
