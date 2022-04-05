from multiprocessing import reduction
import time
import random
import requests


def measure_time(func):
    """
    Простой декоратор, подменивающий возвращаемое значение декорируемой функции на время её выполнения. 

    """
    def inner_function(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return end - start
    return inner_function


@measure_time
def some_function(a, b, c, d, e=0, f=2, g='3'):
    """
    Example function for measure_time decorator.
    """
    time.sleep(a)
    time.sleep(b)
    time.sleep(c)
    time.sleep(d)
    time.sleep(e)
    time.sleep(f)
    return g


def function_logging(func):
    """
    Декоратор, позволяющий логировать запуски функций, распечатывая входные данные и тип возвращаемых значений.
    """
    def inner_function(*args, **kwargs):
        if kwargs :
            kw_print = [f'{key}={value}' for key, value in zip(kwargs.keys(), kwargs.values())]

        if args and kwargs:
            print(f'Function {func.__name__} is calles with pisitional arguments {args} and keyword arguments: {", ".join(kw_print)}.')
        
        elif  args:
            print(f'Function {func.__name__} is calles with pisitional arguments {args} and no keyword.')
            
        elif  kwargs:
            print(f'Function {func.__name__} is calles with no pisitional arguments and keyword arguments: {", ".join(kw_print)}.')

        else:
            print(f'Function {func.__name__} is calles with no arguments.')

        result = func(*args, **kwargs)
        print(f'Function {func.__name__} returns output of type {type(result).__name__}.')
        return result

    return inner_function


@function_logging
def func1():
    """
    Example function for function_logging decorator.
    """
    return set()


@function_logging
def func2(a ,b, c):
    """
    Example function for function_logging decorator.
    """
    return (a + b) / c


@function_logging
def func3(a ,b, c, d=4):
    """
    Example function for function_logging decorator.
    """
    return [a + b * c] * d


@function_logging
def func4(a=None, b=None):
    """
    Example function for function_logging decorator.
    """
    return {a: b}


def russian_roulette_decorator(probability=0.2, return_value='Ooops, your output has been stolen!'):
    """
    Декоратор, русская рулетка, который сделает так, чтобы декорируемая функция 
    с заданной вероятностью заменяла возвращаемое значение на переданное декоратору.
    """
    def dec_func(func):
        def inner_function(*args, **kwargs):
            if random.random() < probability:
                return return_value

            else:
                result = func(*args, **kwargs)
                return result

        return inner_function
    return dec_func


@russian_roulette_decorator(probability=0.2, return_value='Ooops, your output has been stolen!')
def make_request(url):
    """
    Example function for russian_roulette_decorator decorator.
    """
    return requests.get(url)


if __name__ == '__main__':
    # Example run for measure_time decorator
    #print(some_function(1, 2, 3, 4, e=5, f=6, g='9999'))
    
    # Example run for function_logging decorator
    #print(func1(), end='\n\n')
    #print(func2(1 ,2, 3), end='\n\n')
    #print(func3(1 ,2, c=3, d=2), end='\n\n')
    #print(func4(a=None, b=float("-inf")), end='\n\n')

    # Example run for russian_roulette_decorator decorator
    #for _ in range(10):
    #    print(make_request('https://google.com'))
