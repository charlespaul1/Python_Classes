# list declaration
# integers
list1 = [1, 2, 3, 4, 5]
# strings
list2 =['a', 'b', 'c', 'd', 'e']
# different data types
list3 = [1, 'a', 2, 'b', 3, True, 'c', 4, 'd', 5, 6.33,  'e']
# nested lists
list4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# printing items of a list
print(*list1)
# printing the way it is displayed in the code
print(list1)

#  adding items to a list
# using insert, you specify the index to add the item
list1.insert(len(list1), 9)
print(list1)
list1.insert(-1 ,23)
print(list1)
# using append, you dont have to specify the index
list1.append(45)
print(list1)
# using extend,it can accept a list
list1.extend([2,3,4,7,78,23,56,87,10])
print(list1)

# removing something from a list
# using  pop, specify the location index of the item to remove
list1.pop(4)
print(list1)
# using del, specify the index to delete
del list1[3]
print(list1)
# iterating through a list
for item in list2:
    print("value: ",item)