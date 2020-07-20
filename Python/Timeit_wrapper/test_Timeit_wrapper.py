import unittest
from Timeit_wrapper import test_word

# python3 -m unittest tests/test_vglib_gender.py
class TestMethods(unittest.TestCase):

    def test_gensim_add_dict_fail(self):
        print("=== Test 01 begins ===")
        self.assertEqual(0, 0)
