#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

__ = None


class AboutIfStatements(unittest.TestCase):

    def test_if_statement_one(self):

        result = 'original'

        if True:
            result = 'updated'

        assert 'updated' == result

    def test_if_statement_two(self):

        result = 'original'

        if False:
            result = 'updated'

        assert 'original' == result

    def test_if_else_one(self):

        result = 'original'

        if True:
            result = 'updated by True branch'
        else:
            result = 'updated by False branch'

        assert 'updated by True branch' == result

    def test_if_else_two(self):

        result = 'original'

        if False:
            result = 'updated by True branch'
        else:
            result = 'updated by False branch'

        assert 'updated by False branch' == result

    def test_if_then_elif_else(self):

        vowels = 'aeiou'

        letter = 'f'

        if letter in vowels:
            result = 'is vowel'
        else:
            result = 'not vowel'

        assert 'not vowel' == result
