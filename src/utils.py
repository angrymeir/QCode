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
            # TODO: Implement once Matrix class is implemented
            pass
        else:
            raise NotImplementError

    def __rmul__(self, b):
        if type(b) == Vector:
            return self.__mul__(b)
        elif type(b) in [int, float]:
            return [val * b for val in self.values]
        elif type(b) == Matrix:
            # TODO: Implement once Matrix class is implemented
            pass
        else:
            raise NotImplementedError

        
    def dimension(self):
        return len(self.values)
