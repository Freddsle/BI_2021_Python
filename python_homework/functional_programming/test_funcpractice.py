# pytest python_homework\functional_programming
import pytest  # noqa: F401; pylint: disable=unused-variable
import numpy as np
from functional_programming import functional


def test_sequential_map():
    assert functional.sequential_map(np.square, np.sqrt, lambda x: x**3, [1, 2, 3, 4, 5]) == [1, 8, 27, 64, 125]
    assert functional.sequential_map(lambda x: x**2, [1, 2]) == [1, 4]
    assert functional.sequential_map(lambda x: x**2, []) == []


def test_consensus_filter():
    assert functional.consensus_filter(lambda x: x > 0, lambda x: x > 5, lambda x: x < 10, [-2, 0, 4, 6, 11]) == [6]
    assert functional.consensus_filter(lambda x: x > 0, [-2, 0, 4, 6, 11]) == [4, 6, 11]
    assert functional.consensus_filter(lambda x: x > 0, []) == []


'''def test_conditional_reduce():
    assert functional.conditional_reduce(lambda x: x < 5, lambda x, y: x + y, [1, 3, 5, 10]) == 4


def test_func_chain():
    my_chain = functional.func_chain(lambda x: x + 2, lambda x: x/4, x//4)
    assert my_chain(37) == (9.75, 9)


def test_multiple_partial():
    ax1_mean, ax1_max, ax1_sum = functional.multiple_partial(np.mean, np.max, np.sum, axis=1)
    assert None'''
