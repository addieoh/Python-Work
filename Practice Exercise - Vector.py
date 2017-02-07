import math
import operator

class Vector:
    def __init__(self, v):
        self.v = v

    def as_list(self):
        return (self.v)

    def size(self):
        return(len(self.v))

    def magnitude(self):
        return (sum(i ** 2 for i in self.v) ** 0.5)

    def euclidean_distance(self, other):
        a = 0
        for i in range(len(self.v)):
            a += ((self.v[i] - other.v[i])**2)
        return (a ** 0.5)

    def normalized(self):
        b = []
        for i in range(len(self.v)):
            b += [self.v[i] / self.magnitude()]
        return Vector(b)

    def cosine_similarity(self, other):
        sumxx, sumxy, sumyy = 0, 0, 0
        for i in range(len(self.v)):
            x = self.v[i]; y = other.v[i]
            sumxx += x*x
            sumyy += y*y
            sumxy += x*y
        return sumxy/math.sqrt(sumxx*sumyy)

    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self.v) == len(other.v):
                for i in range(len(self.v)):
                    self.v[i] += other.v[i]
                return Vector(self.v)
            else:
                return None
        else:
            return None
            
    def __sub__(self, other):
        if isinstance(other, Vector):
            if len(self.v) == len(other.v):
                for i in range(len(self.v)):
                    self.v[i] -= other.v[i]
                return Vector(self.v)
            else:
                return None
        else:
            return None

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.v) == len(other.v):
                for i in range(len(self.v)):
                    self.v[i] *= other.v[i]
                return (sum(self.v))
            else:
                return None
        elif isinstance(other, int):
            for i in range(len(self.v)):
                self.v[i] = self.v[i] * other
            return Vector(self.v)
        elif isinstance(other, float):
            for i in range(len(self.v)):
                self.v[i] = self.v[i] * other
            return Vector(self.v)
        else:
            return None

    def __truediv__(self, other):
        if isinstance(other, int):
            for i in range(len(self.v)):
                self.v[i] = self.v[i] / other
            return Vector(self.v)
        elif isinstance(other, float):
            for i in range(len(self.v)):
                self.v[i] = self.v[i] / other
            return Vector(self.v)
        else:
            return None
