class Sphere:
    def __init__(self, dim = 3):
        self.dim = dim
        
    def f(self, x):
        y = sum(map(lambda i: i**2, x))
        return y
