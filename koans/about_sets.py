#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from runner.koan import __


class AboutSets(unittest.TestCase):

    def test_sets_make_keep_lists_unique(self):

        highlanders = [
            'MacLeod', 'Ramirez', 'MacLeod', 'Matunas',
            'MacLeod', 'Malcolm', 'MacLeod'
        ]

        there_can_only_be_only_one = set(highlanders)

        self.assertEqual({'MacLeod', 'Ramirez', 'MacLeod', 'Matunas',
            'MacLeod', 'Malcolm', 'MacLeod'}, there_can_only_be_only_one)

    def test_empty_sets_have_different_syntax_to_populated_sets(self):

        self.assertEqual(set((1, 2, 3)), {1, 2, 3})
        self.assertEqual(set(), set())

    def test_creating_sets_using_strings(self):

        self.assertEqual(set(['12345']), {'12345'})
        self.assertEqual({'12345'}, set(['12345']))

    def test_convert_the_set_into_a_list_to_sort_it(self):

        self.assertEqual(['1', '2', '3', '4', '5'], sorted(set('12345')))

    def test_set_have_arithmetic_operators(self):

        scotsmen = {'MacLeod', 'Wallace', 'Willie'}
        warriors = {'MacLeod', 'Wallace', 'Leonidas'}

        self.assertEqual({'Willie'}, scotsmen - warriors)
        self.assertEqual({'Willie', 'Leonidas', 'Wallace', 'MacLeod'}, scotsmen | warriors)
        self.assertEqual({'MacLeod', 'Wallace'}, scotsmen & warriors)
        self.assertEqual({'Willie', 'Leonidas'}, scotsmen ^ warriors)

    def test_we_can_query_set_membership(self):

        self.assertEqual(True, 127 in {127, 0, 0, 1})
        self.assertEqual(True, 'cow' not in set('apocalypse now'))

    def test_we_can_compare_subsets(self):

        # Note that whitespace between parentheses
        # is ignored in python so we can let our
        # parameters span multiple lines for readability.

        self.assertEqual(
            True,
            set('cake') <= set('cherry cake')
        )
        self.assertEqual(
            True,
            set('cake').issubset(set('cherry cake'))
        )
        self.assertEqual(
            False,
            set('cake') > set('pie')
        )
