
def func_chain(*args):
    '''
    The function accepts any number of functions as arguments (positional arguments, NOT a list).
    The function returns a function that concatenates all passed in sequential execution.
    For example:
    my_chain = func_chain(lambda x: x + 2, lambda x: (x/4, x//4)).
    my_chain(37) -> (9.75, 9).
    '''
    def inside_chain_func(inside_container):
        if not inside_container:
            return inside_container

        if isinstance(inside_container, (int, float)):
            for function in args:
                inside_container = function(inside_container)

        else:
            for function in args:
                inside_container = list(map(function, inside_container))

        return inside_container

    return inside_chain_func


def sequential_map(*args):
    '''
    The function accepts as arguments any number of functions (positional arguments, NOT a list),
    as well as a container with some values.
    The function returns a list of the results of sequential application
    of the passed functions to the values in the container.
    For example: sequential_map(np.square, np.sqrt, lambda x: x**3, [1, 2, 3, 4, 5]) -> [1, 8, 27, 64, 125]
    '''
    new_container_values = args[-1]
    now_func_chain = func_chain(*args[:-1])
    return now_func_chain(new_container_values)


def consensus_filter(*args):
    '''
    The function accepts as arguments any number of functions (positional arguments, NOT a list)
    that return True or False, as well as a container with some values.
    The function returns a list of values that, when passed to all functions, give True.
    For example: consensus_filter(lambda x: x > 0, lambda x: x > 5, lambda x: x < 10, [-2, 0, 4, 6, 11]) -> [6]
    '''
    new_container_values = args[-1]

    if not new_container_values:
        return new_container_values

    for function in args[:-1]:
        new_container_values = list(filter(function, new_container_values))

    return new_container_values


def conditional_reduce(func_one, func_two, values):
    '''
    The function takes 2 functions and also a container with values.
    The first function must take 1 argument and return True or False,
    the second takes 2 arguments and returns a value (just like in a normal reduce function).
    conditional_reduce returns one value - the result of reduce,
    skipping the values with which the first function returned False.
    For example, conditional_reduce(lambda x: x < 5, lambda x, y: x + y, [1, 3, 5, 10]) -> 4
    '''
    new_container_values = list(filter(func_one, values))

    if not values:
        return values

    if len(new_container_values) == 1:
        return float(*new_container_values)

    for i in range(len(new_container_values)):
        if i == 0:
            new_number = new_container_values[i]
        else:
            new_number = func_two(new_number, new_container_values[i])

    return new_number


def create_partial(func, **inside_args):
    '''
    Create new functions with predefined values for multiple_partial.
    '''
    def inside_func(*args, **kwargs):
        return func(*args, **inside_args, **kwargs)
    return inside_func


def multiple_partial(*args, **inside_args):
    '''
    This is analogous to the partial function, which takes an unlimited number of functions as arguments
    and returns a list of the same number of "partial functions".
    For example:
    ax1_mean, ax1_max, ax1_sum = multiple_partial(np.mean, np.max, np.sum, axis=1)
    '''
    result = []

    for func in args:
        result.append(create_partial(func, **inside_args))

    return result


def main():
    pass


if __name__ == '__main__':
    main()
