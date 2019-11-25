#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

__ = None


class AboutLoopStatements(unittest.TestCase):

    def test_building_a_new_transformed_list(self):

        phrase = ["fish", "and", "chips"]

        result = []
        for word in phrase:
            result.append(word.upper())

        assert ['FISH', 'AND', 'CHIPS'] == result

    def test_building_a_new_transformed_list_again(self):

        round_table = [
            ["Lancelot", "Blue"],
            ["Galahad", "I don't know!"],
            ["Robin", "Blue! I mean Green!"],
            ["Arthur", "Is that an African Swallow or Amazonian Swallow?"],
        ]

        result = []
        for knight, answer in round_table:
            result.append("Contestant: '" + knight + "' Answer: '" + answer + "'")

        assert result[0] == ("Contestant: 'Lancelot' Answer: 'Blue'")
        assert result[1] == ("Contestant: 'Galahad' Answer: 'I don't know!'")
        assert result[2] == ("Contestant: 'Robin' Answer: 'Blue! I mean Green!'")
        assert result[3] == ("Contestant: 'Arthur' Answer: 'Is that an African Swallow or Amazonian Swallow?'")

    def test_for_with_conditional_filters_a_list(self):

        pythons = [
            ("John Cleese", 1939),
            ("Terry Gilliam", 1940),
            ("Eric Idle", 1943),
            ("Michael Palin", 1943),
        ]

        born_after_1941 = []
        for comedian, age in pythons:
            if age > 1941:
                born_after_1941.append(comedian)

        assert born_after_1941 == ["Eric Idle", "Michael Palin"]

    def test_while(self):

        i = 1
        result = 1
        while i <= 10:
            result = result + i
            i = i + 1

        assert 56 == result

    def test_while_with_break(self):

        i = 1
        result = 1
        while True:
            if i > 10:
                break
            result = result + i
            i = i + 1

        assert 56 == result

    def test_while_with_continue(self):

        i = 0
        result = []
        while i < 10:
            i = i + 1
            if (i % 2) == 0:
                continue
            result.append(i)

        assert [1, 3, 5, 7, 9] == result
