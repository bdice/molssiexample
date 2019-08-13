"""
Unit and regression test for the molssiexample package.
"""

# Import package, test suite, and other packages as needed
import molssiexample
import pytest

@pytest.mark.parametrize(['n', 'answer'], [(0, 1), (1, 2), (2, 2.5), (3, 2.6666667)])
def test_euler(n, answer):
    assert molssiexample.euler(n) == pytest.approx(answer, abs=1e-6)

if __name__ == '__main__':
    pytest.main()
