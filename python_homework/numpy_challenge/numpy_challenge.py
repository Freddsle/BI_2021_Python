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

    list_len = len(matrixes_list)

    if list_len > 1:

        status_check, product = dimension_check(matrixes_list[0].shape, matrixes_list[1].shape)
        
        while status_check:
            for i in range(2, list_len):
                status_check, product = dimension_check(product, matrixes_list[i].shape)

    return status_check


def main():

    array_one = np.random.rand(3, 5)
    array_two = np.linspace(0, 7, 8)
    array_three = np.eye(5)


if __name__ == '__main__':
    main()
