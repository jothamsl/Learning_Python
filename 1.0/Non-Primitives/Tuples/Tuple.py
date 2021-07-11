# A Tuple is a fixed-length, immutable sequence of Python objects. 
# The easiest way to create on is with a comma-separated sequence of values:

tup = 4, 5, 6
print(tup)

# When defining tuples in more complicated expressions, it's often necessary 
# to enclose the values in parentheses, as in this example of creating a tuple of tuples:

nested_tup = (4, 5, 6), (7, 8)
print(nested_tup)

literal_tup = tuple([4, 2, 1, 9])
print(literal_tup)
