#dictionary:  A dictionary in Python is a collection of key-value pairs
# In Dictionary key is must be unique and immutable (like string, number, tuple)
# in dictionary duplicate key are not allowed or overwritten

data = {
    "name": "Hiloni",
    "Address": "ahmedabad",
    "contact": 3333333333
}

print(data)
print(data["name"])

# get value using key
print(data.get("contact"))
print(data.get("Address", "not found"))
print(data.get("xx", "not found"))

# another way to pair keys and values
Keys = ["city", "state", "country"]
values = ["ahmedabad", "Gujarat", "India"]

Disc = zip(Keys,values)
disc = dict(Disc)
print(disc)

#add key and value in existing list
data["location"] = "Navrangpura"
print(data)

#delete key and value from the list
del(data["location"])
print(data)

#another disc
prog = {
    "JS": "Atom",
    "CS": "VS",
    "Python": ["pycharm", "sublime"],
    "Java": {
        "JSE": "Hello",
        "JEE": "world"
    }
}

print(prog)
print(prog["Python"])
print(prog["Python"][0])
print(prog["Java"]["JEE"])
