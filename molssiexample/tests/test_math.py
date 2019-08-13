"""
Unit and regression test for the molssiexample package.
"""

# Import package, test suite, and other packages as needed
import molssiexample as me
import pytest

@pytest.mark.parametrize(['n', 'answer'], [(0, 1), (1, 2), (2, 2.5), (3, 2.6666667)])
def test_euler(n, answer):
    assert me.euler(n) == pytest.approx(answer, abs=1e-6)

def test_euler_failures():
    with pytest.raises(ValueError):
        me.euler(-1)

def test_pi():
    assert me.pi(int(1e6)) == pytest.approx(3.14159, abs=1e-2)

if __name__ == '__main__':
    pytest.main()
