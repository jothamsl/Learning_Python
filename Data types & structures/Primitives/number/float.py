# Floats are floating point numbers. you can use it for rational numbers,
# usually ending with a decimal figure, E.g 1.11 or 3.14
# Optionally, the character e or E followed by a positive or negative integer
# may be appended to specify scientific notation.

# Floats
x = 4.20
y = 1.3
z = 3e-1

# Addition
print(x + y)

# Subtraction
print(x - y)

# Multiplication 
print(x * y)

# Returns the quotient
print(x / y)

# Returns the remainder 
print(x % y)

# Absolute value
print(abs(x))

# x to the power of y
print(x ** y)

# Scientific notation
print(z) # 0.3

# Almost all platforms represent float values as 64-bit "Double-precision"
# values, according to the IEEE 754 standard. In that case, the maximum value a
# floating-point number can have is approximately 1.8x10^308. Python will
# indicate a number greater than that by the string "inf":

print(1.79e308) # 1.79e+308
print(1.8e308)  # inf

# Anything closest a nonzero number can be to zero is approximately 5.0x10^-324

print(5e-324) # 5e-324 
print(1e-325) # 0.0 

# Floating point numbers are represented internally as binary (base-2)
# fractions. Most decimal fractions cannnot be represented exactly as binary
# fractions, so in most cases the internal representation of a floating-point
# number is an approximation of the actual value. In practice, the difference
# between the actual value and the represented value is very small and should
# not usually cause significant problems.
