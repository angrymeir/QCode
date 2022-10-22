import unittest
from src.utils import Vector, Matrix

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

    def test_vector_matrix_multiplication(self):
        value = [1,2]
        ma_val = [[1,2], [3,4]]
        correct_result = [5,11]

        v = Vector(value)
        m = Matrix(ma_val)
        result = v*m

        self.assertEqual(correct_result, result)

    def test_vector_invalid_multiplication(self):
        value = [1,2]

        v = Vector(value)

        self.assertRaises(NotImplementedError, v.__mul__, "LOLWUT")

    def test_vector_vector_rmultiplication(self):
        value1 = [1,2]
        value2 = [3,4]
        correct_result = 11

        v1 = Vector(value1)
        v2 = Vector(value2)
        result = v1.__rmul__(v2)

        self.assertEqual(correct_result, result)

    def test_vector_invalid_rmultiplication(self):
        value = [1,2]

        v = Vector(value)

        self.assertRaises(NotImplementedError, v.__rmul__, "LOLWUT")


class TestMatrix(unittest.TestCase):
    def test_matrix_generation(self):
        value = [[1,2,3], [4,5,6]]
        
        m = Matrix(value)

        self.assertEqual(value, m.values)
        self.assertRaises(TypeError, Matrix, [1,2])

    def test_matrix_generation_dimension_misfit(self):
        value = [[1,2,3], [4,5]]

        self.assertRaises(ValueError, Matrix, value)

    def test_matrix_dimension(self):
        value = [[1,2,3], [4,5,6]]
        correct_row_dim = 2
        correct_col_dim = 3

        m = Matrix(value)
        row_dim = m.dimension('row')
        col_dim = m.dimension('column')
        
        self.assertEqual(correct_row_dim, row_dim)
        self.assertEqual(correct_col_dim, col_dim)
        self.assertRaises(NotImplementedError, m.dimension, 'LOLWUT')

    def test_matrix_check_dimensions(self):
        value_1 = [[1,2,3], [4,5,6]]
        value_2 = [[1,2,3], [4,5,6]]
        value_3 = [[1,2], [4,5]]

        m1 = Matrix(value_1)
        m2 = Matrix(value_2)
        m3 = Matrix(value_3)
        res = m1.check_dimensions(m2)

        self.assertTrue(res)
        self.assertRaises(ValueError, m1.check_dimensions, m3)

    def test_matrix_transpose(self):
        value = [[1,2,3], [4,5,6]]
        correct_result = [[1, 4], [2,5], [3,6]]

        m = Matrix(value)
        result = m.transpose()

        self.assertEqual(correct_result, result)

    def test_matrix_addition(self):
        value1 = [[1,2,3], [4,5,6]]
        value2 = [[1,2,3], [4,5,6]]
        correct_result = [[2,4,6], [8,10,12]]

        m1 = Matrix(value1)
        m2 = Matrix(value2)
        result = m1+m2

        self.assertEqual(correct_result, result)

    def test_matrix_scalar_multiplication(self):
        value = [[1,2,3], [4,5,6]]
        scalar = 2
        correct_result = [[2,4,6],[8,10,12]]

        m = Matrix(value)
        result = m*scalar

        self.assertEqual(correct_result, result)

    def test_matrix_vector_multiplication(self):
        value = [[1,2,3],[4,5,6]]
        vec = [2,3]
        correct_result = [14,19,24]

        m = Matrix(value)
        v = Vector(vec)
        result = m*v

        self.assertEqual(correct_result, result)

    def test_matrix_matrix_multipliaction(self):
        value1 = [[1,2],[3,4]]
        value2 = [[5,6], [7,8]]
        correct_result = [[23,34],[31,46]]

        m1 = Matrix(value1)
        m2 = Matrix(value2)
        result = m1*m2

        self.assertEqual(correct_result, result)

    def test_matrix_invalid_multipliaction(self):
        value = [[1,2], [3,4]]

        m = Matrix(value)

        self.assertRaises(NotImplementedError, m.__mul__, "LOLWUT")
