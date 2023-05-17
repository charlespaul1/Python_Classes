def divide_by(a, b):
    return a / b
try:
    ans = divide_by(10, 0)
except Exception as e:
    print("Something went wrong: ", e)

items = [1,2,3,4,5]
try:
    item = items[6]
except Exception as e:
    print(e, " :Item does not exist in the list")

