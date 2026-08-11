# tuple is almost same as list
# but the difference is in list we can change the value it means list is mutable and in tuple we can't change the value it means tuple is un-mutable
# in short tuple don't support the item assignment


tup = (11, 22, 33, 11, 11, 45)
print(tup)

# indexing number
print(tup[1])

# For Tuple we have two methods
# 1. count : Returns how many times a specific value appears in the tuple.
# 2. index : Returns the index (position) of the first occurrence of a value in the tuple.

# count method
print(tup.count(11))

# index method
print(tup[0])
