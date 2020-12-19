# Strings are sequences of character data. The string type in python is called
# "str". String lirerals may be delimited using either single or double quoted.
# All the characters between the opening delimiter and matching closing
# delimiter are part of the string:

print("I am a string") # I am a string 

print(type("I am a string")) # <class 'str'>

print('I am also a string') # I am also a string 

print(type('I am too')) # <class 'str'> 

# A string in python can contain as many characters as you wish. The only limit
# is your machine's memory resources. A string can also be empty:

print('') # ''

# What if you want to include a quote character as part of the string itself?
# Your first impulse might be to try something like this:

# print('This string contains a single quote (') character.') 
# SyntaxError: invalid syntax

# As you can see, that doesn't work so well. The string in this example opens
# with a single quote, so Python assumes the next single quote, the one in the
# parentheses which was intended to be part of the string, is the closing
# delimiter. The final single quote is then a stray and causes the SyntaxError
# shown.

# If you want to include either type of quote character within the string, the
# simplest way is to delimit the string with the other type. If a string is to
# contain a single quote, delimit it with double quotes and vice versa:

print("This string contains a single quote (') character.")
# This string contains a single quote (') character.

print('This string contains a double quote (") character')
# This string contains a double quote (") character.

#
# ESCAPE SEQUENCES IN STRINGS
#

# Sometimes, you want Python to interpret a character or sequence of characters
# within a string differently. This may occur in one of two ways:

#
# 1. You may want to suppress the special interpretation that certain
#    characters are usually given within a string
# 2. You may want to apply special interpretation to certain characters in a
#    string which would normally be take literally.
 
# You can accomplish this using a backslash (\) character. A backslash
# character in a string indicates that one or more characters that follow it
# should be treated specially. (This is referred to as an escape sequence,
# because the backslash causes the subsequent character sequence to "escape"
# its usual meaning.)

# Let's see how this works.

#
# SUPRESSING SPECIAL CHARACTER MEANING 
#
# You have already seen the problems you can come up against when you try to
# include quote characters in string. If a string is delimited by single
# quotes, you can't directly specify a single quote character as part of the
# string because, for that string, the single quote has special meaning - it
# terminates the string:


