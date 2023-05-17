file = open('test.txt', 'r')
data = file.readline()
print(data)
file.close()
# using the with open function which is better at exception handling and will close the file for you
with open('test.txt', 'r') as file:
    data = file.readline()
    print(data)