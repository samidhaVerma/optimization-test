import numpy as np

class Rastringin:
    def __init__(self, a = 10):
        self.a = a
        
    def f(self, x):
        y = self.a * len(x) + sum(map(lambda i: i**2 - self.a * np.cos(2*np.pi*i), x))
        return y
