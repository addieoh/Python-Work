class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def size(self):
        return (len(self.mat), len(self.mat[0]))

    def get(self, r, c):
        return self.mat[r][c]

    def set(self, r, c, val):
        self.mat[r][c] = val

    def row(self, n):
        return self.mat[n]

    def col(self, n):
        return [row[n] for row in self.mat]

    def transpose(self):
        return Matrix([self.col(i) for i in range(self.size()[1])])

    def add(self, other):
        rows, cols = self.size()
        if isinstance(other, Matrix):
            if (rows, cols) != other.size():
                return None
            return Matrix([[self.get(r,c)+other.get(r,c) for c in range(cols)] for r in range(rows)])
        else:
            return Matrix([[self.get(r,c)+other for c in range(cols)] for r in range(rows)])

    def sub(self, other):
        return self + (other * -1)

    def mul(self, other):
        if isinstance(other, Matrix):
            myrows, mycols = self.size()
            throws, thcols = other.size()
            if mycols != throws:
                return None
            out = [[0 for c in range(thcols)] for r in range(myrows)]
            for r in range(myrows):
                for c in range(thcols):
                    out[r][c] = sum([self.get(r,i)*other.get(i,c) for i in range(mycols)])
            return Matrix(out)
        else:
            rows, cols = self.size()
            return Matrix([[self.get(r,c)*other for c in range(cols)] for r in range(rows)])

    def __sub__(self, other):
        return self.sub(other)

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)


#This subclass shows an alternate implementation of relevant methods
#How is this implementation representing the matrix?
#When might this implementation be preferable?
class SparseMatrix(Matrix):
    def __init__(self, mat):
        self.r = len(mat)
        self.c = len(mat[0])
        self.nonzero = {}
        for i in range(self.r):
            for j in range(self.c):
                val = mat[i][j]
                if val != 0:
                    self.nonzero[(i,j)] = val

    def size(self):
        return (self.r, self.c)

    def get(self, r, c):
        return self.nonzero.get((r,c), 0)

    def set(self, r, c, val):
        if val == 0:
            if (r,c) in self.nonzero:
                del self.nonzero[(r,c)]
        else:
            self.nonzero[(r,c)] = val

    def row(self, n):
        return [self.get(n,i) for i in range(self.c)]

    def col(self, n):
        return [self.get(i,n) for i in range(self.r)]
