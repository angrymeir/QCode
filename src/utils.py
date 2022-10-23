from itertools import groupby

class ComplexNumber:
    def __init__(self, real_part, complex_part):
        self.real_part = real_part
        self.complex_part = complex_part

    def conjugate(self):
        return self.real_part, self.complex_part * -1

    def __add__(self, b):
        if not type(b) == ComplexNumber:
            raise TypeError
        return self.real_part + b.real_part, self.complex_part + b.complex_part

    def __mul__(self, b):
        if not type(b) == ComplexNumber:
            raise TypeError
        real_part = self.real_part*b.real_part - self.complex_part*b.complex_part
        complex_part = self.real_part*b.complex_part + self.complex_part*b.real_part
        return real_part, complex_part

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
