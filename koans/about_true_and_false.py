#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from runner.koan import __


def is_true(condition):

    if condition:
        return 'true stuff'
    else:
        return 'false stuff'


class OnTruthAndFalseness(unittest.TestCase):

    # All the following are considered False

    #def test_true_is_true(self):
        # note calling of function defined
        # outside of the class

        #self.assertEqual(__, is_true(True))

    #def test_false_is_false(self):

        #self.assertEqual(__, is_true(False))

    def test_none_is_considered_false(self):

        self.assertFalse(False)

    def test_zero_is_considered_false(self):

        self.assertFalse(False)

    def test_empty_collections_are_considered_false(self):

        empty_list = []
        empty_set = set()
        empty_dictionary = {}
        empty_tuple = ()

        self.assertFalse(False, empty_list)
        self.assertFalse(False, empty_set)
        self.assertFalse(False, empty_dictionary)
        self.assertFalse(False, empty_tuple)

    def test_blank_strings_are_considered_false(self):

        empty_string = ""

        self.assertTrue(True, empty_string)

    # Everything else is considered True

    def test_everything_else_is_considered_as_true(self):

        self.assertFalse(False, 1)
        self.assertFalse(False, (1))
        self.assertFalse(False, "Python is named after Monty Python")
        self.assertFalse(False, ' ')
        self.assertFalse(False, '0')


"""
Question:

Why have different object types considered as False?
"""
