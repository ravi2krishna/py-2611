# Working With JSON Files / Data 

import json 

student = {
    "id":"101",
    "name":"Ravi",
    "email":"ravi2krishna@gmail.com",
    "courses":["python","ai","cloud"],
    "gpa":9.3
}

print(type(student))
print(student)

print("=" * 50)

# Write Data To JSON File 
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data)
    
print("=" * 50)

# Write Data To JSON File With Indentation
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data,indent=4)
    
print("=" * 50)

# Read Data From JSON File 
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
    print(data)
    print(type(data))
    
print("=" * 50)

# Requirement: Get Student Name & Number Of Courses he joined from student.json file
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
    print(type(data))
    print(data)
    
print("Student Name: ",data['name'])
print("Student Joined Courses: ",data['courses'])
print("Total Number Of Courses Enrolled By Student: ",len(data['courses']))

print("=" * 50)

# Requirement: Check If Student Passed Or Not, based on GPA above 7 from student.json 
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
    print(type(data))
    print(data)
    
if data['gpa'] > 7:
    print("Student Passed")
else:
    print("Student Failed")
    
print("=" * 50)

# File Based -> dump() & load()

# Object Based -> dumps() & loads()

student = {
    "id":"101",
    "name":"Ravi",
    "email":"ravi2krishna@gmail.com",
    "courses":["python","ai","cloud"],
    "gpa":9.3
}

print(type(student))

# dumps(): Convert a native Python dictionary into a formatted JSON string
print("After")
json_data = json.dumps(student)
print(type(json_data))
print(json_data)

print("=" * 50)

# loads(): Convert JSON string back into Python dictionary
json_string = '{"id": "101", "name": "Ravi", "email": "ravi2krishna@gmail.com", "courses": ["python", "ai", "cloud"], "gpa": 9.3}'
print(type(json_string))
py_dict = json.loads(json_string)
print(py_dict)
print("After")
print(type(py_dict))

# Assume i'm a full stack developer 
# Requirement: We have an API, when requested we are getting JSON Data 
# https://dummyjson.com/
# https://dummyjson.com/users

import requests

response = requests.get('https://dummyjson.com/users')
print(response.text) 
print(type(response.text))

api_data = json.loads(response.text)
print(type(api_data))
print(api_data)

# Requirements: Find Number Of Users in the platform 
all_users = api_data['users']
print(all_users)
print(type(all_users))
print("Number Of Users In Platform: ",len(all_users))

# Requirements: Get User ID and Usernames 
for user in all_users:
    print(user)
    print("=" * 50)
    
for user in all_users:
    print(user['id'], user['username'])
 
print("=" * 50)   

# Requirements: Fetch all the usernames Of "Young Users" in the platform i.e aged below 30
print("=" * 50)
print("     Young Users In Platform")
print("=" * 50)
for user in all_users:
    if user['age'] < 30:
        print(user['id'], user['username'], user['age'])