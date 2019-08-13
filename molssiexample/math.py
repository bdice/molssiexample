import numpy as np

def euler(n: int):
    """
    Compute an approximation of e, Euler's number, using Taylor series.

    Parameters
    ----------
    n : int
        Number of terms to use in Taylor series approximation.

    Returns
    -------
    e_approx : float
        Approximation of e.
    """
    if n < 0:
        raise ValueError('Must use a non-negative value for n.')
    e_approx = np.sum([1/np.math.factorial(i) for i in range(n+1)])
    return e_approx

def pi(n: int):
    """
    Compute an approximation of pi using Monte Carlo sampling.

    Parameters
    ----------
    n : int
        Number of Monte Carlo samples.

    Returns
    -------
    pi_approx : float
        Approximation of pi.
    """
    pi_approx = 4 * np.mean(np.linalg.norm(np.random.rand(n, 2), axis=-1) < 1)
    return pi_approx
