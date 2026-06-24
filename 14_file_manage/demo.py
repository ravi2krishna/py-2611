# File Management Using Python 

# Syntax - 1
# file = open("file_path","mode")

# file_data = open("14_file_manage/filenew.txt","r") # FileNotFoundError: [Errno 2] No such file or directory: '14_file_manage/filenew.txt'
file_data = open("14_file_manage/file.txt","r")
print(file_data)

print(file_data.closed) # False --> Still Open 
print(file_data.close()) # Flush and close the IO object.
print(file_data.closed) # True --> Now Closed 

print("=" * 50)

# Syntax - 2 (Recommended)
# with open("file_path","mode") as alias_name:

with open("14_file_manage/file.txt","r") as file_data:
    print(file_data)
print(file_data.closed) # True --> Now Closed Automatically 

print("=" * 50)

# Read Whole Data 
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.read())
    
print("=" * 50)
    
# Read Data Character Wise
with open("14_file_manage/file.txt","r") as file_data:
    for character in file_data.read():
        print(character)

print("=" * 50)

# Read Data Word Wise
with open("14_file_manage/file.txt","r") as file_data:
    for word in file_data.read().split():
        print(word)

print("=" * 50)
    
# Read Data First Line
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.readline())
    
print("=" * 50)

# Read Data Multiple Line
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.readlines())

print("=" * 50)

# Read Data Multiple Line with line wise
with open("14_file_manage/file.txt","r") as file_data:
    for line in file_data.readlines():
        print(line.strip())

print("=" * 50)