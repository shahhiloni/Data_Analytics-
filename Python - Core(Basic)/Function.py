# Defining a Function

def greet():
    print("Hello, welcome to Python!")

# Calling a Function
greet()

# Function with Parameters
def greet(name):
    print(f"Hello, {name}!")


greet("Hiloni")

# Function with Return Value

def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)  # Output: Sum: 8

# Default Parameter Values

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Hiloni")

# Keyword Arguments
def student_info(name, age):
    print(f"{name} is {age} years old.")

student_info(age=22, name="Hiloni")

# Lambda Functions (Anonymous)

square = lambda x: x * x
print(square(5))

# Nested Functions

def outer():
    def inner():
        print("This is inner function.")
    inner()

outer()

# Pass by Reference

def add_item(lst):
    lst.append(4)

items = [1, 2, 3]
add_item(items)
print(items)

#### Example of function in python

## Temperature Converter

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_c = 37
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

## Fibonacci Series

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(6):
    print(fibonacci(i), end=" ")







