# Practise with decorators in Python

1. ```staticmethod_analog``` - Decorator similar to Python defaul staticmethod decorator.\
    Class `Apple` - Example class for staticmethod_analog decorator. Create Apple object with `about_apple` staticmethod - it prints 'Apple is good for you.'

2. ```dataclass_analog``` - Decorator similar to Python defaul dataclass decorator.\
        Args: cls - a class to decorate.\
        Returns: NEW_CLASS - a class that create the object of passed class.\
    If the class already defines `__repr__`, `__eq__` or `__match_args__`, this method do not overwrite.\
    Class `InventoryItem` - Example class for dataclass_analog decorator. Class for keeping track of an item in inventory.

3. ```measure_time``` - decorator that replaces the return value of the function being decorated for the duration of its execution.\
    `some_function` - Example function for `measure_time` decorator.

4. ```function_logging``` - The decorator that allows you to log function runs by printing out the input data and return type.\
    `func1`, `func2`, `func3`, `func4 - Example functions for `function_logging` decorator.

5. ```russian_roulette_decorator``` - Decorator, Russian roulette, which replaces the returned value of decorated function with the one passed to the decorator with a given probability.

    Args inner_function:\
        - probability: a probability for replace.\
        - return_value: string with value for replace.\
    Return:\
        - dec_func: function that return inner_function that return return_value or func return value.

    `make_request` - example function for russian_roulette_decorator decorator.

Examples in `if __name__ == '__main__` block.

# Install and run with pip
## Installation

```console
git clone https://github.com/Freddsle/BI_2021_Python
cd ./BI_2021_Python/python_homework/decorators_practice

# Create and activate your virtual environment

# create virtual environment
python3.10 -m venv ./venv

# activate virtual environment
source ./venv/bin/activate

# if you install it not from main or master, change branch
git checkout decorators_practice

# required by pip to build wheels
pip install wheel==0.37.0 

# Install requirements
pip install -r ./requirements.txt
```

## Run file
```console
python3.10 dec.py
```

# Install and run with poetry
```console
# install poetry
# for details look for https://python-poetry.org/docs/
sudo apt-get install curl
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3.10 -

# poetry will be accessible in current session
source $HOME/.poetry/env

# prepare project (if you have previously installed poetry - start here)
git clone https://github.com/Freddsle/BI_2021_Python
cd ./BI_2021_Python/python_homework/decorators_practice

# if you install it not from main or master, change branch
git checkout decorators_practice

poetry env use python3.10
poetry install

# Run
poetry run python dec.py
```