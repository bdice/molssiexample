"""
Unit and regression test for the molssiexample package.
"""

# Import package, test suite, and other packages as needed
import molssiexample
import pytest

def test_euler():
    assert molssiexample.euler(2) == 2
