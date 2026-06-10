# Tuples 

# empty tuple
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

empty_tuple = tuple()
print(empty_tuple)
print(type(empty_tuple))

# Tuple With Numeric Data 
data = (10,20,30,40,50)
print(data)

# Tuple With Text Data 
data = ("python","ai","cloud")
print(data)

# Tuple With Mixed Data 
data = (10,20,30,"python","ai",1.5,True)
print(data)

# Access Data In Tuples 
data = (10,20,30,40,50)
print(data)

# First Element 
data = (10,20,30,40,50)
first_element = data[0]
print("First Element",first_element)

last_element = data[-1]
print("Last Element",last_element)

# unknown_element = data[10] # IndexError: tuple index out of range
# print(unknown_element)

# Slicing in Tuples is same as Strings 
data = (10,20,30,40,50)
print(data)

print(data[::]) # 10, 20, 30, 40, 50
print(data[1:3:]) # 20,30
print(data[0:5:2]) # 10,30,50

# Access Individual Elements 
data = (10,20,30,40,50)
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])


# Access Individual Elements  -> 10k elements 
data = (10,20,30,40,50,1000000)
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
# print(data[9999999])

print("=" * 20)

# Access Individual Elements  -> 10k elements 
data = (10,20,30,40,50,1000000)
# print(dir(data)) # __iter__ 
for num in data:
    print(num)

print("=" * 20)

# Apply Operators -> Requirement: Multiply Each Element With 10 
data = (10,20,30,40,50)
for num in data:
    print(num * 10)

print("=" * 20)

# Apply Operators -> Requirement: Give Courses In Upper Case    
data = ("python","ai","cloud")
print(data)
for course in data:
    print(course.upper())

print("=" * 20)

# Apply Conditionals -> Requirement: Give Only Even Numbers 
data = (10,20,35,40,55)
for num in data:
    if num % 2 == 0:
        print(num)
        
print("=" * 20)

# Duplicates Allowed & Insertion Order Preserved 
data = (10,20,10,30,10,40,10)
print(data)

# Tuple Operations 
print(dir(data))

# NOTE: New Requirement is to store multiple employees PAN's Do not allow users to update PAN_ID 
# PAN 
pan_ids = ("PAN1234567A","PAN2345678B","PAN3456789C","PAN4567890D","PAN5678901E")
print(pan_ids)
pan_ids[0] = "PAN1111111A" # TypeError: 'tuple' object does not support item assignment
print(pan_ids)