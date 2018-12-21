import pytest
from travis_explore import my_add, inc


def test_my_add():
    assert 3 == my_add(1, 2)


def test_inc():
    assert 3 == inc(2)
