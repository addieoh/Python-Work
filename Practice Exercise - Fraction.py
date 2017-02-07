from fractions import Fraction

class Rational:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def get_numerator(self):
        return self.n

    def get_denominator(self):
        return self.d

    def to_float(self):
        return (self.n / self.d)

    def reciprocal(self):
        return Rational(self.d, self.n)

    def reduce(self):
        c = Fraction(self.n, self.d).limit_denominator()
        return Rational(c.numerator, c.denominator)

    def __add__(self, other):
        if isinstance(other, int):
            return Rational((self.n + other * self.d), self.d)
        elif isinstance(other, float):
            return ((self.n / self.d) + other)
        elif isinstance(other, Rational):
            a = self.d
            b = other.d
            return Rational(self.n * b + other.n * a, a * b)
        else:
            return None

    def __mul__(self, other):
        if isinstance(other, int):
            return Rational(self.n * other, self.d)
        elif isinstance(other, float):
            return ((self.n / self.d) * other)
        elif isinstance(other, Rational):
            return Rational((self.n * other.n), (self.d * other.d))
        else:
            return None
        
    def __truediv__(self, other):
        if isinstance(other, int):
            return Rational(self.n, self.d * other)
        elif isinstance(other, float):
            return ((self.n / self.d) / other)
        elif isinstance(other, Rational):
            return Rational((self.n * other.d), (self.d * other.n))
        else:
            return None

        
    def __sub__(self, other):
        if isinstance(other, int):
            return Rational((self.n - other * self.d), self.d)
        elif isinstance(other, float):
            return ((self.n / self.d) - other)
        elif isinstance(other, Rational):
            a = self.d
            b = other.d
            return Rational(self.n * b - other.n * a, a * b)
        else:
            return None
