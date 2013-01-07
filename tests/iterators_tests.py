import unittest
from itertools import starmap
from pywertools.iterators import (limit_iter, offset_iter, consecutive,
    arithmethic_progression)


class FunctoolsTestCase(unittest.TestCase):

    def test_limit_offset(self):
        list0 = range(0, 1000)
        list1 = list(offset_iter(limit_iter(list0, 400), 100))
        list2 = list(limit_iter(offset_iter(list0, 100), 300))
        list3 = range(100, 400)
        self.assertListEqual(list1, list3)
        self.assertListEqual(list2, list3)

    def test_arithmethic_progression(self):
        list1 = list(arithmethic_progression(range(0, 1001), 3, 1))
        list2 = range(1, 1001, 3)
        self.assertListEqual(list1, list2)

    def test_consecutive(self):
        list0 = range(0, 100)
        diff = lambda a, b: b - a
        list1 = list(starmap(diff, consecutive(list0)))
        list2 = list(starmap(diff, consecutive(list0, step=2)))
        self.assertListEqual(list1, [1] * 99)
        self.assertListEqual(list2, [2] * 49)
