# List Methods / Operations 

# append(): Adds Element To End Of List 
data = [10,20,30,40,50]
print(data)
data.append(60)
print(data)

# extend(): Add Iterable To List 
data = [10,20,30,40,50]
print(data)
data.extend([60,70,80])
print(data)

# insert(): Add element on a specific position based on index 
data = [10,20,40,50]
print(data)
# data.append(30)
data.insert(2,30)
print(data)

# pop(): Removes an element, by default last element 
# If index is provided, removes specific element 
data = [10,20,30,40,50]
print(data)
data.pop()
print(data)

data = [10,20,30,40,50]
print(data)
data.pop(2)
print(data)

# data = [10,20,30,40,50]
# print(data)
# data.pop(10) # IndexError: pop index out of range
# print(data)

# remove(): Removes Element Based On Value
data = [10,20,30,40,50]
print(data)
# data.remove(0) # ValueError: list.remove(x): x not in list
data.remove(20)
print(data)

# Remove 10
data = [10,20,10,30,10,40,10]
print(data)
data.remove(10)
print(data)

# Remove All 10's
data = [10,20,10,30,10,40,10]
print(data)
for num in data:
    if num == 10:
        data.remove(num)
print(data)
        
        
# Remove All 10's
data = [10,20,10,30,10,40,10]
print(data)
while 10 in data:
    data.remove(10)
print(data)    

# clear(): Removes All Elements and Empties List
data = [10,20,30,40,50]
print(data)
data.clear()
print(data)

# index(): Used To Get Index Position Of Given Element
data = [10,20,30,40,50]
print(data)
data.index(30)
print(data.index(30))
print(data.index(50))

# count():  Count the number of occurrences of a value
data = [10,20,10,30,10,40,10]
print(data)
data.count(10)
print(data.count(10))

# reverse(): Reverses The List 
data = [10,20,30,40,50]
print(data)
data.reverse()
print(data)

# sort(): Sorts the list in ascending order 
data = [10,20,40,30,50]
print(data)
data.sort()
print(data)

data = [10,20,40,30,50]
print(data)
data.sort(reverse=True) # descending order 
print(data)

# copy(): Creates a copy of list 
data = [10,20,30,40,50]
print(data)
backup = data.copy()
print(backup)
