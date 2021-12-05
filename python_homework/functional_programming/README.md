Practice with functional programming.

Contained functions:
- **func_chain()** - accepts any number of functions as arguments (positional arguments) and returns a function that concatenates all passed in sequential execution.
- **sequential_map()** - accepts as arguments any number of functions (positional arguments) as well as a container with some values. And returns a list of the results of sequential application of the passed functions to the values in the container.
- **consensus_filter()** - accepts as arguments any number of functions (positional arguments) that return True or False, as well as a container with some values. And returns a list of values that, when passed to all functions, give True.
- **conditional_reduce()** - takes 2 functions and also a container with values. The first function must take 1 argument and return True or False,    the second takes 2 arguments and returns a value. Function returns one value - the result of reduce, skipping the values with which the first function returned False.
- **multiple_partial()** - this is analogous to the partial function, which takes an unlimited number of functions as arguments and returns a list of the same number of "partial functions".