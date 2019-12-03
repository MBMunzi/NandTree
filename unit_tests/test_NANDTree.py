"""Test Module for NANDTree Class
    
    from root directory run (you must follow the test pattern name test_*):
    python3 -m unittest discover -s ./unit_tests -p "test_*.py"
"""

import unittest
from NANDTree import NANDTree


class TestNandTree(unittest.TestCase):

    def test_create_tree_with_invalid_value_should_raise_exception(self):
        exception_text = 'Invalid input for NAND tree. Leaves length must be multiple of two.'
        with self.assertRaisesRegex(Exception, exception_text):
            new_tree = NANDTree(2, [0, 1, 3])

    def test_evaluate_simple_with_correct_parameters_should_return_correct_result(self):
        level_2_tree = NANDTree(2, [1, 1])
        self.assertEqual(0, level_2_tree.evaluate_simple())
