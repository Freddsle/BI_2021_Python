# pytest ./python_homework/numpy_challenge/
import pytest  # noqa: F401; pylint: disable=unused-variable
from numpy_challenge import numpy_challenge
import numpy as np

a_1 = np.array([1.0, 2.0, 3.0])
a_2 = np.array([[2, -5], [3, 6]])
a_3 = np.array([[1, 3], [-2, 4]])

b = np.dtype('int32').type(2.0)

a_big = np.arange(3 * 4 * 5 * 6).reshape((3, 4, 5, 6))
b_big = np.arange(3 * 4 * 5 * 6)[::-1].reshape((5, 4, 6, 3))
c_big = np.arange(5 * 4 * 5 * 4).reshape((5, 4, 4, 5))
big_result = np.dot(a_big, b_big)


def test_matrix_multiplication():
    assert (numpy_challenge.matrix_multiplication(a_3, a_2) == np.array([[11, 13], [8, 34]])).all()
    assert numpy_challenge.matrix_multiplication(b, b) == 4
    assert numpy_challenge.matrix_multiplication(a_1, a_1) == 14.0
    assert (numpy_challenge.matrix_multiplication(b, a_3) == np.array([[2, 6], [-4, 8]])).all()
    assert (numpy_challenge.matrix_multiplication(a_1, b) == np.array([2., 4., 6.])).all()
    assert numpy_challenge.matrix_multiplication(a_big, b_big)[2, 3, 2, 1, 2, 2] == 499128
    assert numpy_challenge.matrix_multiplication(a_1, a_2) is None


def test_dimension_check():
    assert numpy_challenge.dimension_check(a_3.shape, a_2.shape) == (True, (2, 2))
    assert numpy_challenge.dimension_check(b.shape, b.shape) == (True, ())
    assert numpy_challenge.dimension_check(a_1.shape, a_1.shape) == (True, ())
    assert numpy_challenge.dimension_check(b.shape, a_3.shape) == (True, (2, 2))
    assert numpy_challenge.dimension_check(a_1.shape, b.shape) == (True, (3,))
    assert numpy_challenge.dimension_check(a_big.shape, b_big.shape) == (True, (3, 4, 5, 5, 4, 3))
    assert numpy_challenge.dimension_check(a_1.shape, a_2.shape) == (False, None)


def test_multiplication_check():
    assert numpy_challenge.multiplication_check([a_3, a_2]) is True
    assert numpy_challenge.multiplication_check([b, b]) is True
    assert numpy_challenge.multiplication_check([b, b, b, b]) is True
    assert numpy_challenge.multiplication_check([a_1, a_1]) is True
    assert numpy_challenge.multiplication_check([b, a_3]) is True
    assert numpy_challenge.multiplication_check([a_1, b]) is True
    assert numpy_challenge.multiplication_check([a_big, b_big]) is True
    assert numpy_challenge.multiplication_check([a_1, b, a_1, b]) is True
    assert numpy_challenge.multiplication_check([]) is False
    assert numpy_challenge.multiplication_check([a_1, a_2]) is False


def test_multiply_matrices():
    assert (numpy_challenge.multiply_matrices([a_3, a_2]) == np.array([[11, 13], [8, 34]])).all()
    assert (numpy_challenge.multiply_matrices([b, b, b, b]) == 16).all()
    assert (numpy_challenge.multiply_matrices([a_1, a_1]) == 14.0).all()
    assert (numpy_challenge.multiply_matrices([a_1, b]) == np.array([2., 4., 6.])).all()
    assert (numpy_challenge.multiply_matrices([a_big, b_big]) == big_result).all()
    assert (numpy_challenge.multiply_matrices([a_1, b, a_1, b]) == 56.0).all()
    assert numpy_challenge.multiply_matrices([b_big, a_1, b_big, a_1, c_big]).shape == (5, 4, 5, 5, 4, 5)
    assert numpy_challenge.multiply_matrices([]) is None
    assert numpy_challenge.multiply_matrices([a_1, a_2]) is None


def test_compute_2d_distance():
    assert numpy_challenge.compute_2d_distance(np.array([-1, 7]), np.array([7, 1])) == 10
    assert (numpy_challenge.compute_2d_distance(np.array([0, 1]), np.array([2, -2])) - np.sqrt(13)) < 10**(-5)
    assert numpy_challenge.compute_2d_distance(np.array([2, 4]), np.array([0])) is None
    assert numpy_challenge.compute_2d_distance(np.array([2, 4, 0]), np.array([-1, 8])) is None
    assert numpy_challenge.compute_2d_distance(a_2, a_3) is None


def test_compute_multidimensional_distance():
    assert numpy_challenge.compute_multidimensional_distance(np.array([-1, 7]), np.array([7, 1])) == 10
    assert (numpy_challenge.compute_multidimensional_distance(np.array([-1, 7, 3, 5]), 
                                                              np.array([7, 1, 2, 3])) - np.sqrt(105)) < 10**(-5)
    assert numpy_challenge.compute_multidimensional_distance(np.array([2, 4]), np.array([0])) is None
    assert numpy_challenge.compute_multidimensional_distance(np.array([2, 4, 0]), np.array([-1, 8])) is None
    assert numpy_challenge.compute_multidimensional_distance(np.array([2, 4, 0]), np.array([-1, 8])) is None
    assert numpy_challenge.compute_multidimensional_distance(a_2, a_3) is None
