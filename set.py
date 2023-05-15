my_set = {5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10}
print(my_set)
# adding contents to a set
# using add
my_set.add(11)
print(my_set)
# removing items from a ser
my_set.remove(5)
print(my_set)
my_set.discard(6)
print(my_set)
# using math operations on sets
# union join of set
set_one = {1, 2, 3, 4, 5}
set_two = {6, 7, 8, 9, 10}
print(set_one.union(set_two))
# using the vertical bar
print(set_one | set_two)
# getting the items that match in two sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a.intersection(set_b))
# using the ampersand symbol
print(set_a & set_b)
# getting a difference between two sets
# getting elements that are in set a and not b
print(set_a.difference(set_b))
# using the minus symbol to find the difference
print(set_a - set_b)
# getting the symmetric difference
print(set_a.symmetric_difference(set_b))
# using the   carrot operator to get symmetrical difference
print(set_a ^ set_b)


