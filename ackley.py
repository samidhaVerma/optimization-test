import numpy as np

class Ackley:
    def __init__(self, a = 20, b = 0.2, c = 2*np.pi):
        self.a = a
        self.b = b
        self.c = c
        
    def f(self, x):
        dim = len(x)
        term1 = -1. * self.a * np.exp(-1. * self.b * np.sqrt((1./dim) * sum(map(lambda i: i**2, x))))
        term2 = -1. * np.exp((1./dim) * (sum(map(lambda j: np.cos(self.c * j), x))))
        
        return term1 + term2 + self.a + np.exp(1)
