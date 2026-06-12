# Set Methods / Operations 

data = {10,20,30,40,50}
print(type(data))
print(data)

# add(): add element to set 
data.add(60)
print(data)

# update(): add iterable / multiple elements to set 
data = {10,20,30,40,50}
print(data)
data.update([60,70,80,90])
print(data)

# pop(): Removes Random Element 
data = {10,20,30,40,50}
print(data)
data.pop()
print(data)

# remove(): Removes Element By value
data = {10,20,30,40,50}
print(data)
data.remove(30)
# data.remove(300) # KeyError: 300
print(data)

# discard(): same as remove(), Removes Element By value, if no value no Error
data = {10,20,30,40,50}
print(data)
data.discard(30)
data.discard(300) # No KeyError: 300 unlike remove()
print(data)

# clear(): Empties the Set
data = {10,20,30,40,50}
print(data)
data.clear()
print(data)

# copy(): Create a copy 
data = {10,20,30,40,50}
print(data)
backup = data.copy()
print(backup)