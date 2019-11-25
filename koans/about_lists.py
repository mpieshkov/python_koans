#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

__ = False


class AboutLists(unittest.TestCase):

    def test_creating_lists(self):

        empty_list = []

        assert list == type(empty_list)
        assert 0 == len(empty_list)

    def test_accessing_list_elements(self):

        noms = ['peanut', 'butter', 'and', 'jelly']

        assert 'peanut' == noms[0]
        assert 'jelly' == noms[3]

    def test_slicing_lists(self):

        noms = ['peanut', 'butter', 'and', 'jelly']

        assert ["peanut"] == noms[0:1]
        assert ['peanut', 'butter'] == noms[0:2]
        assert ['and', 'jelly'] == noms[2:]
        assert ['peanut', 'butter'] == noms[:2]

    def test_lists_and_ranges(self):

        assert [0, 1, 2] == list(range(3))
        assert [3, 4, 5] == list(range(3, 6))

    def test_insertions(self):

        knight = ['you', 'shall', 'pass']
        knight.insert(2, 'not')
        assert ['you', 'shall', 'not', 'pass'] == knight

        knight.insert(0, 'Arthur')
        assert ['Arthur', 'you', 'shall', 'not', 'pass'] == knight

    def test_popping_lists(self):

        stack = [1, 2, 3]
        stack.append('last')

        assert [1, 2, 3, 'last'] == stack

        popped_value = stack.pop()
        assert 'last' == popped_value
        assert [1, 2, 3] == stack

