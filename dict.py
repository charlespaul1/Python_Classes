# dictionaries
sample_dict = {1: "coffee", 2: "tea", "three": "juice", 4: "milk", 5: 77, 6: 44.23}
# accessing an element in a dictionary using a key
print(sample_dict["three"])
# changing an item in a dictionary
sample_dict [2] = "german"
print(sample_dict[2])
# deleting an item in dictionary
del sample_dict["three"]
print(sample_dict)
# adding items to a dictionary
newDict = {}
newDict["name"] = "Jim"
newDict[2] = "cow"
print(newDict)
# iterating through a dictionary
for key, value in sample_dict.items():
    print(str(key) + ": "+ str(value))