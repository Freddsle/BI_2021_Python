import numpy as np
import traceback


def dimension_check(first_matrix_shape, second_matrix_shape):
    '''
    Checks if matrices can be multiplied by their shapes.
    If yes, it returns the True and product shape.
    If not - False.
    '''

    if len(first_matrix_shape) == 0 or len(second_matrix_shape) == 0:
        shape_to_return = second_matrix_shape if len(first_matrix_shape) == 0 else first_matrix_shape
        return True, shape_to_return

    if len(first_matrix_shape) == 1 and len(second_matrix_shape) == 1:
        return True, ()

    if len(second_matrix_shape) == 1:
        if first_matrix_shape[-1] == second_matrix_shape[-1]:
            shape_to_return = (first_matrix_shape[:-1])
            return True, shape_to_return

    if first_matrix_shape[-1] == second_matrix_shape[-2]:
        shape_to_return = (first_matrix_shape[:-1]) + (second_matrix_shape[:-2]) + tuple([second_matrix_shape[-1]])
        return True, shape_to_return

    return False, None


def matrix_multiplication(first_matrix, second_matrix):
    '''
    Multiplies two matrices.
    '''

    check_status = dimension_check(first_matrix.shape, second_matrix.shape)[0]

    try:

        if check_status:

            if np.isscalar(first_matrix) or np.isscalar(second_matrix):
                print('One/both matrices are O-D matrices (scalar).')
                return np.dot(first_matrix, second_matrix)

            if first_matrix.ndim == 1 and second_matrix.ndim == 1:
                print('Both 1D matrices, return scalar.')
                return np.dot(first_matrix, second_matrix)

            if first_matrix.ndim == 2 and second_matrix.ndim == 2:
                print('Both 2D matrices, multiplied like conventional matrices.')
                return np.matmul(first_matrix, second_matrix)

            print('Returns the dot product of matrices')
            return np.dot(first_matrix, second_matrix)


    except ValueError:
        print('!!!Something wrong with arrays dimensions!!!')
        print('More info:')
        print(traceback.format_exc())


def multiplication_check(matrixes_list):
    '''
    Checks if matrices in matrixes_list can be sequentially multiplied.
    If yes, it returns the True.  If not - False.
    '''

    list_len = len(matrixes_list)

    if list_len > 1:

        status_check, product = dimension_check(matrixes_list[0].shape, matrixes_list[1].shape)

        for i in range(2, list_len):

            if status_check:
                status_check, product = dimension_check(product, matrixes_list[i].shape)

            else:
                break

        return status_check

    return False


def multiply_matrices(matrices_list):
    '''
    Sequentially multiplies the matrices in the list. Returns the result of the multiplication.
    If it cannot multiply, it returns None.
    '''

    list_len = len(matrices_list)

    if multiplication_check(matrices_list):
        product = matrix_multiplication(matrices_list[0], matrices_list[1])

        for i in range(2, list_len):
            product = matrix_multiplication(product, matrices_list[i])

        return product

    else:
        if list_len == 0:
            print('Matrices list contain only one matrix.')

        return None


def compute_2d_distance(first_1D_array, second_1D_array):
    '''
    Calculates the distance between two points on the coordinate plane.
    Points are specified by two one-dimensional numpy arrays of length 2.
    '''

    # shape check
    if len(first_1D_array.shape) != 1 or len(second_1D_array.shape) != 1:
        print('Not 1D arrays!')
        return None

    # len check
    if len(first_1D_array) != 2 or len(second_1D_array) != 2:
        print('There are not two coordinates in one or two arrays.')
        return None

    return np.sqrt((first_1D_array[0] - second_1D_array[0])**2 + (first_1D_array[1] - second_1D_array[1])**2)


def compute_multidimensional_distance(first_N_array, second_N_array):
    '''
    Takes 2 one-dimensional arrays with any number of values (but equal) and calculates the distance between them.
    '''

    # shape check
    if len(first_N_array.shape) != 1 or len(second_N_array.shape) != 1:
        print('Not 1D arrays!')
        return None

    # len check
    if len(first_N_array) != len(second_N_array):
        print('Matrices of unequal length!')
        return None

    return np.linalg.norm(first_N_array - second_N_array)


def compute_pair_distances(obs_2D_array):
    '''
    Takes a 2d array, where each row is an observation and each column is a feature.
    The function calculates and returns a matrix of pairwise distances.
    '''

    if len(obs_2D_array.shape) != 2:
        print('Not 2D arrays!')
        return None

    number_obs = obs_2D_array.shape[0]

    answer_matrix = np.zeros((number_obs, number_obs))

    for i in range(number_obs):
        for j in range(number_obs):

            if i != j:
                answer_matrix[i, j] = compute_multidimensional_distance(obs_2D_array[i], obs_2D_array[j])

    return answer_matrix


def main():

    array_one = np.random.rand(3, 5)
    array_two = np.linspace(0, 7, 8)
    array_three = np.eye(5)

    print('First array:', array_one)
    print('Second array:', array_two)
    print('Therd array:', array_three)


if __name__ == '__main__':
    main()
