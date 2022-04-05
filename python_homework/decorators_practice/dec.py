import time


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




if __name__ == '__main__':
    print(some_function(1, 2, 3, 4, e=5, f=6, g='9999'))
    
