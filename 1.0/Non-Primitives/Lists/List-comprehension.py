# List comprehensions in python are the same as normal lists but, instead of data inside it, you
# enter an expression followed by a 'for' loop and 'if-else' clauses.

# The most basic form of list comprehension in python are:

# list_variable = [expression for item in collection].
# The first expression generates elements in the list followed by a 'for' loop over some collection
# of data which would evaluate the expression for every item in the collection.

# But how do you get to this formula-like way of building and using these constructs in python?

# THE MATH BEHIND IT
# ------------------

# Remember in maths, the common ways to describe lists (or sets, or tuples, or vectors) are:
# S = {x^2: x in {0 ... 9}}, V = (1, 2, 4, 8, ..., 2^12), M = {x | x in S and x even}.

# In other words, you'll find that the above definitions tell you the following:

# -> S is a sequence that contains values between 0 and 9 inclusive, and each value is raised to the
# power of two.

# -> The sequnce V, on the other hand, contains the value 2 that is raised to a certain power x. The
# power x starts from 0 and goes till 12.

# -> Lastly, the sequence M contains only the even elements from the sequence S.

# Now that you've understood some of the math behind lists, you can translate or implement the
# mathematical notation of constructing lists in python using list comprehensions. Take a look at
# the following:

s = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
v = [2**i for i in range(13)]  # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
