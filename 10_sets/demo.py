# Sets 

# empty set
empty_set = {} # Empty Set Cannot be created with Symbol
print(empty_set)
print(type(empty_set))

empty_set = set()
print(empty_set)
print(type(empty_set))

# Set With Numeric Data 
data = {10,20,30,40,50}
print(type(data))
print(data) # Sets are Unordered Collection 

# List With Numeric Data 
data = [10,20,30,40,50]
print(type(data))
print(data) # Lists are Ordered Collection 

# Sets With Text Data 
data = {"python","ai","cloud"}
print(data)

# Sets With Mixed Data 
data = {10,20,30,"python","ai",1.5,True}
print(data)

# First Element 
# data = {10,20,30,40,50}
# first_element = data[0] # TypeError: 'set' object is not subscriptable
# print("First Element",first_element)

# last_element = data[-1]
# print("Last Element",last_element)

# Access Individual Elements - Cannot be done, as no index & no key 
# data = {10,20,30,40,50}
# print(data[0])

print("=" * 20)

# Access Individual Elements  -> 10k elements 
data = {10,20,30,40,50,60,70,80,90,100,1000000}
print(dir(data)) # __iter__ 
for num in data:
    print(num)

print("=" * 20)

# Apply Operators -> Requirement: Multiply Each Element With 10 
data = {10,20,30,40,50}
for num in data:
    print(num * 10)

print("=" * 20)

# Apply Operators -> Requirement: Give Courses In Upper Case    
data = {"python","ai","cloud"}
print(data)
for course in data:
    print(course.upper())

print("=" * 20)

# Apply Conditionals -> Requirement: Give Only Even Numbers 
data = {10,20,35,40,55}
for num in data:
    if num % 2 == 0:
        print(num)
        
print("=" * 20)

# Duplicates Not Allowed & Insertion Order Not Preserved 
data = {10,20,10,30,10,40,10}
print(data)

# Set Operations 
print(dir(data))