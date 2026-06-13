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

# Special Methods Specific to Sets Only (Math Related Sets)
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# union(): Combine Sets
print(s1.union(s2))
print(s1 | s2)

# intersection(): Get Common Elements From Sets 
print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)

# intersection_update(): Get Common Elements From Sets, Updates Calling Set 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.intersection_update(s2))
print(s1)
print(s2)

# difference(): Removes Common Elements From Sets and gives unique elements 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)

# difference_update(): Removes Common Elements From Sets and gives unique elements, Updates Calling Set 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference_update(s2)) 
print(s1)
print(s2)

# symmetric_difference(): Removes Common Elements From Sets and takes combined elements from both sets
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print(s1)
print(s2)

# symmetric_difference_update(): Removes Common Elements From Sets and takes combined elements from both sets, Updates Calling Set 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)

# issubset(): Checks if given set is a subset of another set
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}

print(s2.issubset(s1))
print(s3.issubset(s1))

# issuperset(): Checks if given set is a superset of another set
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}
print(s1.issuperset(s2))
print(s1.issuperset(s3))

# isdisjoint(): Checks if given sets have no common elements 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))