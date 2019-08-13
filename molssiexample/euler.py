import numpy as np

def euler(n: int = 10, x: float = 1):
    return np.sum([x**i/np.math.factorial(i) for i in range(n)])
