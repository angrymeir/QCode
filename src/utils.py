from itertools import groupby


class ComplexNumber:
    def __init__(self, real_part, complex_part):
        self.real_part = real_part
        self.complex_part = complex_part

    def conjugate(self):
        return ComplexNumber(self.real_part, self.complex_part * -1)

    def __add__(self, b):
        if type(b) == int:
            return ComplexNumber(self.real_part + b, self.complex_part)
        elif type(b) == ComplexNumber:
            return ComplexNumber(self.real_part + b.real_part, self.complex_part + b.complex_part)
        else:
            raise TypeError

    def __radd__(self, b):
        return self.__add__(b)

    def __mul__(self, b):
        if type(b) == int:
            real_part = self.real_part*b
            complex_part = self.complex_part*b
        elif type(b) == ComplexNumber:
            real_part = self.real_part*b.real_part - self.complex_part*b.complex_part
            complex_part = self.real_part*b.complex_part + self.complex_part*b.real_part
        else:
            raise TypeError
        return ComplexNumber(real_part, complex_part)

    def __rmul__(self, b):
        if type(b) == int:
            real_part = self.real_part*b
            complex_part = self.complex_part*b
        elif type(b) == ComplexNumber:
            self.__mul__(b)
        else:
            raise TypeError
        return ComplexNumber(real_part, complex_part)

    def __eq__(self, b):
        if isinstance(self, b.__class__):
            return self.real_part == b.real_part and self.complex_part == b.complex_part
        return False

    def __str__(self):
        return "{} {}i".format(self.real_part, self.complex_part)


class Vector:
    def __init__(self, values:list):
        self.values = values

    def __add__(self, b):
        if self.dimension() != b.dimension():
                raise ValueError('Dimensions of vectors do not match: {} and {}'.format(self.dimension(), b.dimension()))

        result = []
        for i in range(self.dimension()):
            result.append(self.values[i] + b.values[i])
        return result

    def __mul__(self, b):
        if type(b) == Vector:
            if self.dimension() != b.dimension():
                raise ValueError('Dimensions of vectors do not match: {} and {}'.format(self.dimension(), b.dimension()))
            result = 0
            for i in range(self.dimension()):
                result +=  self.values[i] * b.values[i]
            return result
        elif type(b) in [int, float]:
            return [val * b for val in self.values]
        elif type(b) == Matrix:
            return Matrix(b.transpose())*self
        else:
            raise NotImplementedError

    def __rmul__(self, b):
        if type(b) == Vector:
            return self.__mul__(b)
        elif type(b) in [int, float]:
            return [val * b for val in self.values]
        else:
            raise NotImplementedError

    def dimension(self):
        return len(self.values)

    def inner_product(self, b):
        if self.dimension() != b.dimension():
            raise ValueError('Dimensions of vectors do not match: {} and {}'.format(self.dimension(), b.dimension())) 
        if type(self.values[0]) == ComplexNumber:
            result = ComplexNumber(0,0)
            for v1,v2 in zip(self.values, b.values):
                result += (v1.conjugate()*v2)
            return result
        else:
            return sum([v1*v2 for v1,v2 in zip(self.values, b.values)])

class Matrix:
    def __init__(self, values):
        # Check if values are list of list
        if type(values) != list or type(values[0]) != list:
            raise TypeError
       
        # Check if all entries in matrix are of same length
        col_length = groupby([len(col) for col in values])
        if not next(col_length, True) or next(col_length, False):
            raise ValueError

        self.values = values

    def check_dimensions(self, b):
        if self.dimension('row') != b.dimension('row') or self.dimension('column') != b.dimension('column'):
            raise ValueError
        return True

    def dimension(self, direction):
        if direction=='row':
            return len(self.values)
        elif direction=='column':
            return len(self.values[0])
        else:
            raise NotImplementedError

    def transpose(self):
        row = self.dimension('row')
        col = self.dimension('column')
        return [[self.values[j][i] for j in range(row)] for i in range(col)]

    def adjoint(self):
        new_matrix = []
        if type(self.values[0][0]) == ComplexNumber:
            for column in self.values:
                new_col = []
                for entry in column:
                    new_col.append(entry.conjugate())
                new_matrix.append(new_col)
            return Matrix(Matrix(new_matrix).transpose())
        return Matrix(self.transpose())

    def determinant(self):
        if self.dimension('row') == 2:
            return self.values[0][0]*self.values[1][1] - self.values[0][1]*self.values[1][0]
        result = 0
        for i in range(self.dimension('row')):
            tmp_result = 1
            for ii in range(self.dimension('column')):
                row_index = (i+ii)%self.dimension('row')
                col_index = ii
                value = self.values[row_index][col_index]
                tmp_result *= value 
            result += tmp_result
        for i in range(self.dimension('row')):
            tmp_result = 1
            for ii in range(self.dimension('column')):
                row_index = (i+ii)%self.dimension('row')
                col_index = self.dimension('column')-1-ii
                value = self.values[row_index][col_index]
                tmp_result *= value
            result -= tmp_result
        return result


    def is_identity(self):
        for i in range(self.dimension('row')):
            for j in range(self.dimension('column')):
                if i != j and self.values[j][i] != 0:
                    return False
                if i == j and self.values[j][i] != 1:
                    return False
        return True

    def is_hermitian(self):
        return self.values == self.adjoint().values

    def is_unitary(self):
        result = Matrix(self.adjoint()*self)
        return result.is_identity()

    def is_normal(self):
        return Matrix(self.adjoint()*self) == Matrix(self * self.adjoint())
       
    def is_orthogonal_projection_matrix(self):
        return self.is_hermitian() and Matrix(self*self) == self

    def is_invertible(self):
        return self.determinant() != 0

    def __add__(self, b):
        self.check_dimensions(b)
        result = []
        for i in range(self.dimension('row')):
            column_a = Vector(self.values[i])
            column_b = Vector(b.values[i])
            result.append(column_a + column_b)
        return result

    def __mul__(self, b):
        if type(b) in [int, float]:
            result = []
            for i in range(self.dimension('row')):
                column = Vector(self.values[i])
                result.append(column*b)
            return result
        elif type(b) == Vector:
            result = []
            cur_matrix = self.transpose()
            for column in cur_matrix:
                result.append(Vector(column)*b)
            return result
        elif type(b) == Matrix:
            result = []
            cur_matrix = self.transpose()
            for col_b in b.values:
                new_col = []
                for col_a in cur_matrix:
                    new_col.append(Vector(col_b)*Vector(col_a))
                result.append(new_col)
            return result
        else:
            raise NotImplementedError

    def __eq__(self, b):
        if isinstance(self, b.__class__):
            return self.values == b.values
        return False
