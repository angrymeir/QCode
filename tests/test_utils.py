import unittest
from src.utils import Vector

class TestVector(unittest.TestCase):

    def test_vector_creation(self):
        values = [1,2,3,4,5]

        v = Vector(values)

        self.assertEqual(v.values, values)

    def test_vector_dimension(self):
        values = [1,2,3,4,5]
        correct_result = len(values)

        v = Vector(values)

        self.assertEqual(correct_result, v.dimension())

    def test_vector_addition_correct(self):
        value_1 = [1,2]
        value_2 = [2,3]
        correct_result = [3,5]

        v1 = Vector(value_1)
        v2 = Vector(value_2)
        result = v1 + v2

        self.assertEqual(correct_result, result)

    def test_vector_addition_dimension_misfit(self):
        value_1 = [1]*3
        value_2 = [1]*2

        v1 = Vector(value_1)
        v2 = Vector(value_2)

        self.assertRaises(ValueError, v1.__add__, v2)

    def test_vector_vector_multiplication_correct(self):
        value_1 = [1,2]
        value_2 = [4,5]
        correct_result = 14

        v1 = Vector(value_1)
        v2 = Vector(value_2)
        result = v1 * v2

        self.assertEqual(correct_result, result)

    def test_vector_vector_multiplication_dimension_misfit(self):
        value_1 = [1]*3
        value_2 = [1]*2

        v1 = Vector(value_1)
        v2 = Vector(value_2)

        self.assertRaises(ValueError, v1.__mul__, v2)

    def test_vector_scalar_multiplication(self):
        value_1 = [1,2]
        scalar = 2
        correct_result = [2,4]

        v1 = Vector(value_1)
        result = v1 * scalar

        self.assertEqual(correct_result, result)

    def test_scalar_vector_multiplication(self):
        value_1 = [1,2]
        scalar = 2
        correct_result = [2,4]

        v1 = Vector(value_1)
        result = scalar * v1

        self.assertEqual(correct_result, result)

