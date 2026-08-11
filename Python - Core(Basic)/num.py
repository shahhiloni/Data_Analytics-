# Note: its mutable which means we can change the value

nums = [89, 80, 22, 11, 34]
print(nums)

# // print first element of the list (according to indexing)
print(nums[0])

# // remove first two elements of the list
print(nums[2:])

# // remove last elements of the list because of minus (its also support minus value and give output accordingly)
print(nums[:-1])

# // append: add elements in the end of list
nums.append(12)
print(nums)

# // insert - add elements in between of the list (first value is index number, and the second value is object which we want to add)
nums.insert(2, 33)
print(nums)

# // remove: remove the element from the list
nums.remove(11)
print(nums)

# //pop: remove the element from the list according given index number or if you don't specify the number of index than it carry last number of the list
nums.pop(3)
print(nums)

# // del: it's show first two elements of the list and delete other elements from the list
del nums[2:]
print(nums)

# // extend:
nums.extend([23, 45, 44])
print(nums)

# // print minimum number of the list
print(min(nums))

# // print maximum number of the list
print(max(nums))

# // total number of the given list - addition
print(sum(nums))

# // sort: change list in Descending order
nums.sort()
print(nums)

# // reverse: change list in Ascending order
nums.reverse()
print(nums)

names = ["john", "jonny", "joy"]
print(names)

value = [12, "Hello world", 45, "Hello Python"]
print(value)

mix = [nums, names, value]
print(mix)