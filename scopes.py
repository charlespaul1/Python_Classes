# global scope
my_global = 5

def func():
    local_v = 10
    print("global variable: ", my_global)


func()