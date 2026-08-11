# Default Arguments - Default values are used if no value is provided by the caller.

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Hiloni")

# Positional Arguments - Values are matched based on their position in the function call.

def info(name, age):
    print(f"{name} is {age} years old.")

info("Asha", 25)  # Output: Asha is 25 years old

# Keyword Arguments - You specify which argument corresponds to which parameter by name.
info(age=22, name="Hiloni")

# Arbitrary Positional Arguments (*args)- used when you're not sure how many arguments will be passed (stored as a tuple).

def add_all(*numbers):
    total = sum(numbers)
    print("Total:", total)

add_all(1, 2, 3)
add_all(10, 20, 30, 40)

# Arbitrary Keyword Arguments (**kwargs) -  Used when you're not sure how many keyword arguments will be passed (stored as a dictionary).

def student_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

student_details(name="Hiloni", age=22, course="Python")

#### Combine all Arguments

def demo(a, b=10, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

demo(5, 20, 30, 40, name="Hiloni", city="Mumbai")


###### Argument order

# def func(positional, /, positional_or_keyword, *, keyword_only):
#     def func(a, b=2, *args, **kwargs):





