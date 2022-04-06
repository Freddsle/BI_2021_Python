import time
import random
from unittest import result
import requests
import re
import inspect


def staticmethod_analog(func):
    """
    Decorator similar to staticmethod.
    """
    @classmethod
    def inner_function(*args, **kwargs):
        return func(*args[1:], **kwargs)
    return inner_function


class Apple:
    """
    Example class for staticmethod_analog decorator.
    """

    def __init__(self, ap_type, number):
        self.ap_type = ap_type
        self.number = number

    @staticmethod_analog
    def about_apple(first=1, second=2):
        print('Apple is good for you.')
        print(first, second)


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


# Реализуйте декоратор аналогичный dataclass.
# Весь функционал сделать как у стандартного dataclass за исключением того, 
# что он не должен принимать дополнительные аргументы. 
# При работе с декораторами классов очень полезными могут оказаться встроенные в питон функции setattr и getattr. 
# Также вам нужно будет найти способ "распарсить" аннотации типов. 

def dataclass_analog(cls):

    class NEW_CLASS(cls):

        def __init__(self, *args, **kwargs) -> None:
            self.__dict__.update(kwargs)
            i = 0

            for key in cls.__annotations__:
                if key not in self.__dict__:
                    setattr(self, key, cls.__annotations__[key](args[i]))
                    i += 1

        def __repr__(self):
            if '__repr__' not in cls.__dict__.keys():
                attrs = [f"{key}={value}" for key, value in self.__dict__.items()]
                return f'{type(self).__name__}({", ".join(attrs)})'
            else:
                return super().__repr__()

        def __eq__(self, other):
            if '__eq__' not in cls.__dict__.keys():
                if other.__class__ is self.__class__:
                    return list(self.__dict__.values()) == list(other.__dict__.values())
                return NotImplemented
            else:
                return super().__repr__()

        def __match_args__(self):
            if '__match_args__' not in cls.__dict__.keys():
                return  tuple(self.__dict__.keys())
                
            else:
                return super().__match_args__()

    NEW_CLASS.__name__ = cls.__name__

    return NEW_CLASS

    
@dataclass_analog   
class InventoryItem:
    """
    Example class for dataclass_analog decorator.
    Class for keeping track of an item in inventory.
    """
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

    # Test for "repr"
    # def __repr__(self) -> str:
    #    return 'Test for "repr" - super.'


if __name__ == '__main__':
    # Example run for measure_time decorator
    # print(some_function(1, 2, 3, 4, e=5, f=6, g='9999'))
    
    # Example run for function_logging decorator
    # print(func1(), end='\n\n')
    #print(func2(1 ,2, 3), end='\n\n')
    #print(func3(1 ,2, c=3, d=2), end='\n\n')
    #print(func4(a=None, b=float("-inf")), end='\n\n')

    # Example run for russian_roulette_decorator decorator
    #for _ in range(10):
    #    print(make_request('https://google.com'))

    # Example run for staticmethod_analog decorator
    #Apple('gold', 5).about_apple()
    #Apple.about_apple()

    # Example run for dataclass_analog decorator
    invemtory = InventoryItem('pen', 23.0, 3)
    print(f'invemtory.name: \t {invemtory.name}')
    print(f'invemtory.unit_price: \t {invemtory.unit_price}')
    print(f'invemtory.quantity_on_hand: \t {invemtory.quantity_on_hand}')
    print(f'invemtory.total_cost: \t {invemtory.total_cost()}')
    print(f'invemtory: \t {invemtory}')

    invemtory2 = InventoryItem('pen', 15.0, 2)
    print(f'invemtory: \t {invemtory.__eq__(invemtory2)}')

    invemtory3 = InventoryItem('pen', 15.0, 2)
    print(invemtory3.__match_args__())