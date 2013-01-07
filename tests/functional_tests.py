import unittest
from pywertools.functional import compose


class FunctoolsTestCase(unittest.TestCase):

    def test_compose(self):
        a = lambda x: x + 2
        b = lambda x: x * 2

        self.assertEqual(compose(a, b)(2), 6)
        self.assertEqual(compose(b, a)(2), 8)
        self.assertEqual(compose(b, a, b)(2), 12)
