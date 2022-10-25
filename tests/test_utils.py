import unittest
from src.utils import Vector, Matrix, ComplexNumber

class TestComplexNumber(unittest.TestCase):
    def test_complex_number_creation(self):
        real, comp = 2,3

        c = ComplexNumber(real, comp)

        self.assertEqual(c.real_part, real)
        self.assertEqual(c.complex_part, comp)

    def test_complex_number_addition(self):
        real_1,comp_1 = 3,2
        real_2,comp_2 = 1,7
        correct_result = ComplexNumber(4,9)

        c1 = ComplexNumber(real_1, comp_1)
        c2 = ComplexNumber(real_2, comp_2)
        result = c1 + c2

        self.assertEqual(correct_result, result)

    def test_complex_number_addition_incorrect(self):
        real,comp = 3,2

        c = ComplexNumber(real, comp)

        self.assertRaises(TypeError, c.__add__, "asdf")

    def test_complex_number_multiplication(self):
        real_1,comp_1 = 3,2
        real_2,comp_2 = 1,7
        correct_result = ComplexNumber(-11,23)

        c1 = ComplexNumber(real_1, comp_1)
        c2 = ComplexNumber(real_2, comp_2)
        result = c1 * c2

        self.assertEqual(correct_result, result)

    def test_complex_number_multiplication_incorrect(self):
        real,comp = 3,2

        c = ComplexNumber(real, comp)

        self.assertRaises(TypeError, c.__mul__, 2.0)

    def test_complex_number_conjugate(self):
        real,comp = 3,2
        correct_result = ComplexNumber(3,-2)

        c = ComplexNumber(real, comp)
        result = c.conjugate()

        self.assertEqual(correct_result, result)


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

    def test_vector_inner_product_real_numbers(self):
        value1 = [1,2]
        value2 = [2,3]
        correct_result = 8

        v1 = Vector(value1)
        v2 = Vector(value2)
        result = v1.inner_product(v2)

        self.assertEqual(correct_result, result)

    def test_vector_inner_product_complex_numbers(self):
        value1 = [ComplexNumber(1,2),ComplexNumber(2,3)]
        value2 = [ComplexNumber(4,5),ComplexNumber(6,7)]
        correct_result = ComplexNumber(47,-7)

        v1 = Vector(value1)
        v2 = Vector(value2)
        result = v1.inner_product(v2)

        self.assertEqual(correct_result, result)


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

    def test_matrix_adjoint(self):
        value = [[ComplexNumber(1,2), ComplexNumber(1,2)], [ComplexNumber(3,4), ComplexNumber(3,4)]]
        correct_result = Matrix([[ComplexNumber(1,-2), ComplexNumber(3,-4)], [ComplexNumber(1,-2), ComplexNumber(3,-4)]])

        m = Matrix(value)
        result = m.adjoint()

        self.assertEqual(correct_result, result)

    def test_matrix_is_hermitian(self):
        value = [[1,0], [0,1]]

        m = Matrix(value)

        self.assertTrue(m.is_hermitian())

    def test_matrix_is_identity(self):
        value = [[1,0], [0,1]]

        m = Matrix(value)

        self.assertTrue(m.is_identity())

    def test_matrix_is_not_identity(self):
        value = [[1, 1], [1,1]]

        m = Matrix(value)

        self.assertFalse(m.is_identity())

    def test_matrix_is_unitary(self):
        value = [[1,0], [0,1]]

        m = Matrix(value)

        self.assertTrue(m.is_unitary())

    def test_matrix_is_not_unitary(self):
        value = [[1,1], [0,1]]

        m = Matrix(value)

        self.assertFalse(m.is_unitary())

    def test_matrix_is_normal(self):
        value = [[1,0], [0,1]]

        m = Matrix(value)

        self.assertTrue(m.is_normal())

    def test_matrix_is_not_normal(self):
        value = [[1,2], [0,1]]

        m = Matrix(value)

        self.assertFalse(m.is_normal())

    def test_matrix_is_orthogonal_projection_matrix(self):
        value = [[1,0], [0,0]]

        m = Matrix(value)

        self.assertTrue(m.is_orthogonal_projection_matrix())

    def test_matrix_is_not_orthogonal_projection_matrix(self):
        value = [[1,2], [0,0]]

        m = Matrix(value)

        self.assertFalse(m.is_orthogonal_projection_matrix())

    def test_matrix_determinant(self):
        value = [[6, 4, 2], [1,-2,8], [1,5,7]]
        correct_result = -306

        m = Matrix(value)
        result = m.determinant()

        self.assertEqual(correct_result, result)

    def test_matrix_determinant_transpose(self):
        value = [[6, 4, 2], [1,-2,8], [1,5,7]]
        m1 = Matrix(value)
        m2 = Matrix(value)

        self.assertEqual(m1.determinant(), Matrix(m2.transpose()).determinant())

    def test_matrix_determinant_multiplication(self):
        value1 = [[6, 4, 2], [1,-2,8], [1,5,7]]
        value2 = [[1, 4, 4], [1,-5,8], [1,3,7]]

        m1 = Matrix(value1)
        m2 = Matrix(value2)
        result1 = Matrix(m1*m2).determinant()
        result2 = m1.determinant()*m2.determinant()

        self.assertEqual(result1, result2)


    def test_is_invertible(self):
        value = [[1,1], [1,0]]

        m = Matrix(value)

        self.assertTrue(m.is_invertible())

    def test_is_not_invertible(self):
        value = [[1,1], [1,1]]

        m = Matrix(value)

        self.assertFalse(m.is_invertible())
