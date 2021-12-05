
def sequential_map(*functions):
    '''
    The function accepts as arguments any number of functions (positional arguments, NOT a list), 
    as well as a container with some values.
    The function returns a list of the results of sequential application of the passed functions to the values in the container. 
    For example: sequential_map(np.square, np.sqrt, lambda x: x**3, [1, 2, 3, 4, 5]) -> [1, 8, 27, 64, 125]
    !!! Дополнительно - интегрировать сюда func_chain.
    '''
    new_container_values = functions[-1].copy()

    for function in functions[:-1]:
        new_container_values = list(map(function, new_container_values))

    return new_container_values


def consensus_filter(*functions):
    '''
    The function accepts as arguments any number of functions (positional arguments, NOT a list) 
    that return True or False, as well as a container with some values.
    The function returns a list of values that, when passed to all functions, give True.
    For example: consensus_filter(lambda x: x > 0, lambda x: x > 5, lambda x: x < 10, [-2, 0, 4, 6, 11]) -> [6]
    '''
    new_container_values = functions[-1].copy()

    for function in functions[:-1]:
        new_container_values = list(filter(function, new_container_values))

    return new_container_values


def conditional_reduce():
    '''
    функция должна принимать 2 функции, а также контейнер с значениями. 
    Первая функция должна принимать 1 аргумент и возвращать True или False, 
    вторая также принимает 2 аргумента и возвращает значение (как в обычной функции reduce). 
    conditional_reduce должна возвращать одно значение - результат reduce, 
    пропуская значения с которыми первая функция выдала False. 
    Например, conditional_reduce(lambda x: x < 5, lambda x, y: x + y, [1, 3, 5, 10]) -> 4
    '''
    pass


def func_chain(*args):
    '''
    функция должна принимать в качестве аргументов любое количество функций (позиционными аргументами, НЕ списком). 
    Функция должна возвращать функцию, объединяющую все переданные последовательным выполнением. 
    Например, 
    my_chain = func_chain(lambda x: x + 2, lambda x: x/4, x//4). 
    my_chain(37) -> (9.75, 9). 
    !!! +2 дополнительных балла за интеграцию этой функции в 1 задание. !!!
    '''
    pass


def multiple_partial(*args):
    '''Реализовать функцию  multiple_partial - аналог функции partial, 
    но которая принимает неограниченное число функций в качестве аргументов и 
    возвращает список из такого же числа "частичных функций". 
    !!! Не используйте саму функцию partial. 
    Например: ax1_mean, ax1_max, ax1_sum = multiple_partial(np.mean, np.max, np.sum, axis=1)
    '''
    pass


def main():
    pass


if __name__ == '__main__':
    main()