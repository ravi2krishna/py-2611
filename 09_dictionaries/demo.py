# Dictionaries 

# empty dictionary
empty_dictionary = {}
print(empty_dictionary)
print(type(empty_dictionary))

empty_dictionary = dict()
print(empty_dictionary)
print(type(empty_dictionary))

# Dictionary With Numeric Data 
data = {1:10,2:20,3:30,4:40,5:50}
print(type(data))
print(data)


# Dictionary With Text Data 
data = {"c1":"python","c2":"ai","c3":"cloud"}
print(type(data))
print(data)

# Dictionary With Mixed Data 
data = {1:10,2:20,3:30,"c1":"python","c2":"ai","gpa":8.5,"passed":True}
print(type(data))
print(data)

# Access Data In Dictionary 
data = {1:10,2:20,3:30,4:40,5:50}
print(data)

# First Element 
# data = {1:10,2:20,3:30,4:40,5:50}
# first_element = data[0] # KeyError: 0
# print("First Element",first_element)

# last_element = data[-1]
# print("Last Element",last_element)

data = {1:10,2:20,3:30,4:40,5:50}
first_element = data[1] # NOTE: This is Key, not index
print("First Element",first_element)

last_element = data[5]
print("Last Element",last_element)

# unknown_element = data[10] # # KeyError: 10
# # print(unknown_element)

# Access Individual Elements 
data = {1:10,2:20,3:30,4:40,5:50}
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])

# Access Individual Elements  -> 10k elements 
data = [10,20,30,40,50,1000000]
data = {1:10,2:20,3:30,4:40,5:50,10000:1000000}
print(data[1])
print(data[2])
print(data[3])
print(data[4])
# print(data[9999999])

print("=" * 20)

# Access Individual Elements  -> 10k elements 
data = {1:10,2:20,3:30,4:40,5:50,10000:1000000}
# print(dir(data)) # __iter__ 
for num in data: # Only Keys We Got
    print(num)

print("=" * 20)

for key in data: # Only Keys We Got
    print(key)

print("=" * 20)

for key in data: # Using Keys Only We Access Value
    print(data[key])

print("=" * 20)