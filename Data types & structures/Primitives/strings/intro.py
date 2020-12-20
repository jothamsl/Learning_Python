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

# print('This string contains a single quote (') character.') 
# SyntaxError: invalid syntax

# Specifying a backslash in front of the quote character in a string "escapes"
# it and causes Python to suppress its usual special meaning. It is then
# interpreted simply as a literal single quote character:

print('This string contains a single quote (\') character.')
# This string contains a single quote (') character.

# \' -- Terminates string with single quote opening delimiter 
# \" -- Terminates string with double quote opening delimiter 
# \newline -- Terminates input line 
# \\ -- Introduces escape sequence 

# Ordinaryly, a newline character terminates line input. So pressing [Enter] in
# the middle of a string will cause Python to think it's incomplete:

# Print('a  SyntaxError: EOL while scanning string literal 

# To break up a string over more than one line, include a backslash before
# each newline, and the newlines will be ignored:

print('a\
        b\
        c') # abc 

# To include a backslash in a string, escape it with a backslash 
 
print('foo\\bar') # foo\bar 

#
# APPLYING SPECIAL MEANING TO CHARACTERS 
#

# Suppose you need to create a string that contains a tab character in it. Some
# text editors may allow you to insert a tab character into your code. But many
# programmers consider that poor practice, for several reasons:
#
# 1. The computer can distinguish between a tab character and a sequence of
# space characters, but you can't.
#
# 2. Some text editors are configured to automatically eliminate tab characters
# by expanding them to the appropriate number of spaces. 
#
# 3. Some Python REPL environments will not insert tabs into code.

# In Python, a tab character can be specified by the escape sequence "\t":

print('foo\tbar') # foo      bar

# \a                           ASCII Bell (BEL) character 
# \b                           ASCII Backspace (BS) character 
# \f                           ASCII Formfeed (FF) character 
# \n                           ASCII Linefeed (LF) character 
# \N{<name>}                   Character from Unicode database with given <name>
# \r                           ASCII Carriage return (CR) character 
# \t                           ASCII Horizontal Tab (TAB) character 
# \uxxxx                       Unicode character with 16-bit hex value xxxx
# \Uxxxxxxxx                   Unicode character with 32-bit hex value xxxxxxxx
# \v                           ASCII Vertical Tab (VT) character 
# \000                         Character with octal value ooo
# \xhh                         Character with hex value hh

# Examples 
print("a\tb") # a    b 

print("a\141\x61") # aaa

print("a\nb") 
# a
# b 

print('\u2192 \N{rightwards arrow}')
# -> ->

# This type of escape sequence is typically used to insert characters that are
# not readily generated from the keyboard or are not easily readable or
# printable. 

#
# RAW STRINGS 
#

# A raw string literal is preceded by r or R, which specifies that escape
# sequensequences in the associated string are not translated.

print('foo\nbar')
# foo
# bar

print(r'foo\nbar') # foo\nbar 
print(R'foo\\bar') # foo\\bar 

#
# TRIPLE-QUOTED STRINGS 
#

# There is yet another way of delimiting strings in Python. Triple-quoted
# strings are delimited by matching groups of three single quotes or three
# double quotes. Escape sequences still work in triple-quoted strings, but
# single quotes, double quotes, and newlines can be included without escaping
# them. This provide a convenient way to create a string with both single and
# double quotes in it:

print ('''This string has a single (') and a double (") quote.''')
# This string has a single (') and a double (") quote. 

# Because newlines can be included without escaping them, this also allows for
# multiline strings:

print("""This is a
string that spans
across several lines
""")
# This is a
# string that spans
# across several lines
