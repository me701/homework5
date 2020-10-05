from math import sqrt

class Vector:

    def __init__(self, n, v=0.0):
        assert n > 0
        self.values = [v]*n
        self.n = n

    def __str__(self):
        return str(self.values)

    def __setitem__(self, i, v):
        self.values[i] = v

    def __getitem__(self, i):
        return self.values[i]

    def __add__(self, X):
        Z = Vector(self.n, 0.0)
        for i in range(self.n):
            Z[i] = self.values[i] + X[i]
        return Z

    @property
    def norm(self):
        return sqrt(sum([i**2 for i in self.values]))

if __name__ == "__main__":

    V = Vector(6, 1)
    Y = Vector(5, 2)

    for i in range(5):

        V[i] = i+1

    Z = V + Y
