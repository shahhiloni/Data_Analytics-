#Without global — You can’t modify global variable inside function

x = 10

def change():
    x = 20   # this creates a new local variable, not changing the global x

change()
print(x)

# With global — You can modify the global variable

x = 10

def change():
    global x
    x = 20   # now we are modifying the global x

change()
print(x)
