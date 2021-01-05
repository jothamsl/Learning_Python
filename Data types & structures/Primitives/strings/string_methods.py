str.casefold
str.upper 
str.lower 
str.capitalize 
str.title 
str.swapcase 

str.casefold 
# ------------

# str.casefold creates a lowercase string that is suitable for case insensitive
# comparisons. This is mroe aggressive than str.lower and may modify strings
# that are already in lowercase or cause strings to grow in length, and is not
# intended for display purposes.

"XßΣ".casefold()
# 'xssσ'

"XßΣ".lower()
# 'xßς'

str.upper()
#----------

# str.upper takes every character in a string and converts it to its uppercase
# equivalent, for example:

"This is a 'string'.".upper()
# "THIS IS A 'STRING'."

str.lower() 
#---------

# str.lower does the opposite; It takes every character in a string and
# converts it to its lowercase equivalent

"This IS a 'string'.".lower()
# "this is a 'string'."

str.capitalize()
#---------------

# str.capitalize returns a capitalized version of the string, that is, it makes
# the first character have uppercase and the rest lower:

"this Is A 'String'.".capitalize()
# "This is a 'string'."

str.title()
#----------

# str.title returns the title cased version of the string, that is, every
# letter in the beginnning of a word is made uppercase and all other are made
# lower case:

"this Is a 'String'".title()
# "This Is A 'String'"

str.swapcase()
#-------------

# str.swapcase returns a new string object in which all lower case characters
# are swapped to upper case and all upper case characters to lower: 

"this iS A STRiNG".swapcase()

# "THIS Is a strIng"

# USAGE OF 'str' CLASS METHODS
# It is worth noting that these methods may be called either on string objects
# (as shown above) or as a class method of the str class (with an explicit call
# to str.upper, etc.) 

str.upper("This is a 'string'")

"THIS IS A 'STRING'"

# This is most useful when applying one of these methods to many strings at
# once in say, a map function 
# NOTE:(A map function applys some function to an object)

map(str.upper, ["These", "are", "some", "'strings'"])
# ['These', 'ARE', 'SOME', "'STRINGS'"]






