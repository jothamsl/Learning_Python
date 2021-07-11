# A list contains items separated by commas and enclosed within square brackets
# []. Lists are almost similar to arrays in C. One difference is that all the
# items belonging to a list can be of different data type. 

list = [21, 'Hello world!', 23.1, 'f']
list1 = ['What up', 'world']
print(list) # [21, 'Hello world!', 23.1, 'f']
print(list[0:2]) # Output's first two elements, [21, 'Hello world!']
print(list1 * 2) # Output's list1 two times, ['What up', 'world', 'What up', 'world']
print(list + list1) # Output's concatenatioon of both the lists 
                    # [21, 'Hello world!', 23.1, 'f', 'What up', 'world']

