# FUNCTIONS
# parameter     | Details
# --------------|--------
# arg1,...,argN | Regular arguments
# *args         | Unnamed positional arguments
# kw1,...,kwN   | Keyword-only arguments
# **kwargs      | The rest of keyword arguments

# Using the def statement is the most common way to define a function in
# python. This statement is a so called 'single clause compound statement' with
# the following syntax:

def function_name(parameters):
    statement(s)

# "function_name" is called the 'identifier' of the function. Since a function
# definition is an executable statement, its execution binds the function name
# to the function object which can be called later on using the identifier

# "Parameters" is an optional list of identifiers that get bound to the values
# supplied as arguments when when the function is called. A function may have
# an arbitrary number of arguments which are separated by commas.

# "statement(s)" also known as the function body are a non-empty sequence of
# statements executed each time the function is called. This means a function
# body cannot be empty, just like any indented block.


def greet():
    print("Hello world!")


greet()  # Hello world!

# This is a another function definition that takes one single argument and
# displays the passed in value each time the function is called:


def greet_two(greeting):
    print(greeting)


greet_two("Wassup")  # Wassup

# Default parameter values can be set in a function:


def greet_three(greeting="Wassup"):
    print(greeting)


greet_three()  # Wassup

# In python, you do not need to explicitly declare a return type of the
# function. Python functions can return values of any type via the 'return'
# keyword. One function can return any number of different types!


def many_types(x):
    if x < 0:
        return "Hello!"
    else:
        return 0


print(many_types(1))  # 0
print(many_types(-1))  # Hello!

# A function that reaches the end of execution without a return statement will
# always return None:


def do_nothing():
    pass  # NOTE: Pass is just a place holder for possible code. It does nothing


print(do_nothing())  # None


# ARBITRARY NUMBER OF FUNCTION ARGUMENTS
# --------------------------------------
# Defining a function capable of taking an arbitrary number of arguments can be
# done by prefixing one of the arguments with an '*'

def func(*args):
    # args will be a tuple containing all values that are passed in
    for i in args:
        print(i)

# Calling it with 3 arguments
func(1, 2, 3) # 1,
              # 2,
              # 3

list_of_arg_values = [1, 2, 3]

 # calling it with list of values, * expands the list
func(*list_of_arg_values) # 1,
                          # 2, 
                          # 3

# Calling it without arguments
func() # No output

# NOTE: You can't provide a default for args, 
# IF you already have your arguments in an array (or any other Iterable), you
# can invoke your function like this: func(*my_stuff)

# These arguments (*args) can be accessed by index, for example args[0] will
# return the first argument

# ARBITRARY NUMBER OF KEYWORD ARGUMENTS 
# -------------------------------------
# You can take an arbitrary number of arguments with a name by defining an
# argument in the definition with two '**' in front of it:

def func2(**kwargs):
    # Kwargs will be a dictionary containing the names as keys and the values
    # as values
    for name, value in kwargs.items():
        print(name, value)

# calling it with 3 arguments 
func2(value1=1, value2=2 , value3=3) # value1 1
                                     # value2 2
                                     # value3 3

# Calling it without arguments
func2() # No output

my_dict = {"foo": 1, 'bar': 2}

# Calling it with a dictionary 
func(**my_dict) # foo 1
                # bar 2


