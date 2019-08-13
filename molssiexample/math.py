import numpy as np

def euler(n: int = 10, x: float = 1):
    if n < 0:
        raise ValueError('Must use a non-negative value for n.')
    return np.sum([x**i/np.math.factorial(i) for i in range(n+1)])

def pi(n: int = 100):
    return 4 * np.mean(np.linalg.norm(np.random.rand(n, 2), axis=-1) < 1)
