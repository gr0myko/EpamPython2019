import unittest
from switch_support import test_function


class SwitchSupportTests(unittest.TestCase):
    def test_expr_in_argument(self):
        result = test_function(11, 9 + 2, 16, 5)
        self.assertEqual(result, 1)

    def test_expr_in_docstring(self):
        result = test_function(17, 11, 13, 16)
        self.assertEqual(result, 4)
