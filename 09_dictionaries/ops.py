# Dictionary Methods / Operations 

data = {"a":"apple","b":"banana"}
print(data)

# update(): adds / updates items in dictionary
data.update({"c":"cherry"}) # adds item if key is not present
print(data)

data.update({"a":"apricot"}) # updates item if key is present
print(data)

# pop(): Removes an item by key 
data = {"a":"apple","b":"banana"}
print(data)
data.pop("a")
print(data)
# data.pop("c") # KeyError: 'c'
# print(data)

# popitem(): Removes last item 
data = {"a":"apple","b":"banana"}
print(data)
data.popitem()
print(data)

# clear(): Empties Dictionary
data = {"a":"apple","b":"banana"}
print(data)
data.clear()
print(data)

# get(): Used to get value by key 
data = {"a":"apple","b":"banana"}
print(data)
data.get("a")
print(data.get("a"))
print(data.get("c")) # None -> No Error, when key is not found 

# keys(): Used To get keys 
data = {"a":"apple","b":"banana"}
print(data)
data.keys()
print(data.keys())

for key in data.keys():
    print(key)
    
# values(): Used To get values 
data = {"a":"apple","b":"banana"}
print(data)
data.values()
print(data.values())

for value in data.values():
    print(value)
    
# items(): Used To get keys and values 
data = {"a":"apple","b":"banana"}
print(data)
data.items()
print(data.items())

for item in data.items():
    print(item)
    
# setdefault(): Returns a value of key, if the key is present 
# If key is not present, then adds the item and returns the value 
data = {"a":"apple","b":"banana"}
print(data)
data.setdefault("b","blueberry")
print(data.setdefault("b","blueberry"))

data = {"a":"apple","b":"banana"}
print(data)
print(data.setdefault("c","cherry"))
print(data)

# copy(): Creates a copy 
data = {"a":"apple","b":"banana"}
print(data)
backup = data.copy()
print(backup)