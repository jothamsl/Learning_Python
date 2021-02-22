# The lambda keyword creates and inline function that contains a single
# expression. The value of this exrpesssion is what the functio returns when
# invoked.

def greeting():
    return "Hello world"

print(greeting()) # Hello world 

# This same function can be written as a lamda function:
greet_me = lambda: "Hello world"
print(greet_me()) # Hello world

# Lambdas can also take arguments:
strip_and_upper_case = lambda s: s.strip().upper()

strip_and_upper_case("Hello") # HELLO

# They can also take arbitrary number of arguments/ keyword arguments, like
# normal functions:
greet = lambda x, *args, **kwargs: print(x, args, kwargs)
greet("hello", 'world', world='world', ) # hello ('world',) {'world': 'world'}
