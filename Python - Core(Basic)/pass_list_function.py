def show_list(items):
    for item in items:
        print(item)

fruits = ["apple", "banana", "cherry"]
show_list(fruits)


## append - modify into function (You can change the list inside the function, and it will affect the original list.)
def add_item(mylist):
    mylist.append("orange")

fruits = ["apple", "banana"]
add_item(fruits)
print(fruits)

## Return a New List (Without Changing Original) - (If you don’t want to change the original list, make a copy)
def new_list_with_item(mylist):
    new_list = mylist.copy()
    new_list.append("mango")
    return new_list

fruits = ["apple", "banana"]
result = new_list_with_item(fruits)
print("Original:", fruits)
print("Modified:", result)

## Sum All List Elements

def total(numbers):
    return sum(numbers)

marks = [80, 75, 90]
print("Total Marks:", total(marks))
