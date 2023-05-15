# declaring a tuple
my_tuple = (1, True, 4.78, "tuple")
# accessing items in a tuple(it is index based)
print(my_tuple[2])
print("number of occurrence of the word tuple: ",my_tuple.count("tuple"))
# checking up an index of an item
print(my_tuple.index(4.78))
# iterating through a tuple
for item in my_tuple:
    print(item)
    