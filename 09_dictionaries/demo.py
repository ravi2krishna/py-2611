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

# Apply Operators -> Requirement: Multiply Each Element With 10 
data = {1:10,2:20,3:30,4:40,5:50}
for key in data:
    print(key * 10)

print("=" * 20)

# Apply Operators -> Requirement: Multiply Each Element With 10 
data = {1:10,2:20,3:30,4:40,5:50}
for key in data:
    print(data[key] * 10)

print("=" * 20)

# Apply Operators -> Requirement: Give Courses In Upper Case    
data = {"c1":"python","c2":"ai","c3":"cloud"}
print(data)
for course in data:
    print(data[course].upper())
    
print("=" * 20)
   
# Apply Conditionals -> Requirement: Give Only Even Numbers 
data = {1:10,2:20,3:35,4:45,5:50}
for key in data:
    if data[key] % 2 == 0:
        print(data[key])
        
print("=" * 20)

# Duplicates Allowed - Values Can be Duplicated & Order Preserved
data = {1:10,2:20,3:30,4:40,5:50,6:20,7:10,8:20,9:20}
print(data)

print("=" * 20)

# Duplicates Allowed - Keys should be Unique, Latest Key will Override Old Key 
data = {1:10,2:20,3:30,1:40,5:20,2:60}
print(data)

print("=" * 20)

# Keys must be immutable objects only
data = {1:10,2:20}
print(data)

print("=" * 20)

# Keys must be immutable objects only
# data = {[1]:10,[2]:20}
# print(data)

# Keys must be immutable objects only, but vales can be any object 
data = {1:[10],2:[20]}
print(data)

print("=" * 20)

# Keys must be immutable objects only
data = {(1):[10],(2):[20]}
print(data)

print("=" * 20)

# Keys must be immutable objects only
data = {"1":10,"2":20}
print(data)

print("=" * 20)

# Immutability Check 
data = {1:10,2:20}
print(data)
data[1] = 100
print(data)

print("=" * 20)

# Real World Dictionaries Looks like JSON Data 
# https://media.licdn.com/dms/image/v2/D4D12AQGwOUMYbhUu-A/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1682148646113?e=2147483647&v=beta&t=qeCSY5Ktzx2jkeq7suYaSBV_-OS_18P-yuabrIhNWcU
# https://www.anbowell.com/_astro/guide_to_json.DimYsN86.webp
# https://www.goanywhere.com/sites/default/files/styles/max_2600x2600/public/2022-08/example_json_file_0.png.webp?itok=nS3qt8dd

students = {"101":{},"102":{}}
print(students)
print(type(students))

print("=" * 20)

students = {
    "101":{
        "name":"Ravi",
        "email":"ravi2krishna@gmail.com",
        "courses":["python","ai","cloud"],
        "courses_fee":(10000,20000,10000)
    },
    "102":{
        "name":"Mike",
        "email":"mike@gmail.com",
        "courses":["java","devops","cloud"],
        "courses_fee":(10000,20000,10000)
    }
}

print(students)
print(type(students))

print("=" * 20)

# Get All Students Details 
print(students)

print("=" * 20)

# Get 101 Student Details 
# print(students[101]) # KeyError: 101, as its int
print(students["101"])

print("=" * 20)

# Get Courses Enrolled by Mike 
print(students["102"])
print(students["102"]["courses"])

print("=" * 20)

# Get 2nd Course Enrolled by Mike 
print("2nd Course ",students["102"]["courses"][1])

print("=" * 20)

# Check if mike is a google customer or not 
if students["102"]['email'].endswith("@gmail.com"):
    print(f"User {students["102"]['name']} is Google Customer")
else:
    print(f"User {students["102"]['name']} is Not Google Customer")

print("=" * 20)

students["102"]['email'] = "mike@outlook.com"   
print(students["102"])

# Check if mike is a google customer or not 
if students["102"]['email'].endswith("@gmail.com"):
    print(f"User {students["102"]['name']} is Google Customer")
else:
    print(f"User {students["102"]['name']} is Not Google Customer")

print("=" * 20)

# Dictionary Operations 
print(dir(students))