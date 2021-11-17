Here are solutions for some of the problems from the [collection of 100 numpy exercises](https://github.com/rougier/numpy-100) in `test_challenge.py` and matrix multiplication functions in `numpy_challenge.py`.

Functions in `numpy_challenge.py`:
- `dimension_check` - Checks if matrices can be multiplied by their shapes. If yes, it returns the True and product shape. If not - False.
- `matrix_multiplication` - Multiplies two matrices.
- `multiplication_check` - Checks if matrices in matrixes_list can be sequentially multiplied. If yes, it returns the True.  If not - False.
- `multiply_matrices` - Sequentially multiplies the matrices in the list. Returns the result of the multiplication. If it cannot multiply, it returns None.
- `compute_2d_distance` - Computes the distance between two points on the coordinate plane. Points are specified by two one-dimensional numpy arrays of length 2.
- `compute_multidimensional_distance` - Takes 2 one-dimensional arrays with any number of values (but equal) and calculates the distance between them.
- `compute_pair_distances` - Takes a 2D array, where each row is an observation and each column is a feature. The function calculates and returns a matrix of pairwise distances.