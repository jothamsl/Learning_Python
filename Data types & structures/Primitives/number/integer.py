# In Python, there is effectively no limit to how long an integer value can be.
# But it is constrained by the amount of memory you system has.
print(12123232123412438247392374298347924723849273849273482937 + 1)

# Integers are used to represent numeric data, and more specifically, whole
# numbers from negative infinity to infinity, E.g 4, 1, 6, -1212, -5

print(type(10))
print(type(0x10))

x = 5
y = 2 

# Addition 
print(x + y)

# Subtraction 
print(x - y)

# Multiplication 
print(x * y)

# Returns the quotient 
print( x / y)

# Returns the remainder 
print(x % y)

# Absolute value 
print(abs(x))

# x to the power of y
print(x ** y)


# The following string s can be prepended to an integer value to indciate a
# base other than 10
#-----------------------------------------------------
#|          Prefix          |  Interpretation | Base | 
#|--------------------------|-----------------|------|
#|0b (zero + lowercase 'b') |     Binary      |  2   |
#|0B (zero + uppercase 'B') |                 |      |
#|                          |                 |      |
#|0o (zero + lowercase 'o') |      Octal      |  8   |
#|0o (zero + uppercase 'O') |                 |      |
#|                          |                 |      |
#|0x (zero + lowercase 'x') |   Hexadecimal   |  16  |
#|0X (zero + uppercase 'X') |                 |      |
#|----------------------------------------------------
# E.g 

print(0o10) # 8

print(0x10) # 16 
 
print(0b10) # 2  
