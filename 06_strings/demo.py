# Strings 

# Single Line Strings
s1 = 'hello' # Recommended
print(s1)
print(type(s1))

s1 = "hello" # Recommended
print(s1)
print(type(s1))

s1 = '''hello''' # Not Recommended
print(s1)
print(type(s1))

s1 = """hello""" # Not Recommended
print(s1)
print(type(s1))

# Multi Line Strings

# define_python = "Python is a high-level, general-purpose programming language 
#         that emphasizes code readability, simplicity, and 
#         ease-of-writing with the use of significant indentation, 
#         "plain English" naming, an extensive ("batteries-included") 
#         standard library, and garbage collection."
# print(define_python)

define_python = '''Python is a high-level, general-purpose programming language 
        that emphasizes code readability, simplicity, and 
        ease-of-writing with the use of significant indentation, 
        "plain English" naming, an extensive ("batteries-included") 
        standard library, and garbage collection.'''
print(define_python)


define_python = """Python is a high-level, general-purpose programming language 
        that emphasizes code readability, simplicity, and 
        ease-of-writing with the use of significant indentation, 
        "plain English" naming, an extensive ("batteries-included") 
        standard library, and garbage collection."""
print(define_python)

# When you use single quote in a string, enclose them in double quotes 
question = "how are you ?"
# answer = 'i'm fine'
answer = "i'm fine"
print(answer)

# When you use double quote in a string, enclose them in single quotes 
question = "how are you ?"
# answer = "i"m fine"
answer = 'i"m fine'
print(answer)

# When you use both single quote and double quote in a string use triple single / double quotes 
question = "how are you ?"
# answer = "i'm fine i"m fine"
answer = '''i'm fine i"m fine'''
answer = """i'm fine i"m fine"""
print(answer)

# Accessing Strings 
text = "python"
print(text)

# Accessing Strings Using Index 
# Positive Indexing - Starts from the beginning of string  i.e index of first character is 0
print(text[0])
print(text[1])
print(text[2])

# Negative Indexing - Starts from the end of string  i.e index of last character is -1 
print(text[-1])
print(text[-2])

# print(text[10]) # IndexError: string index out of range

# Print all characters
text = "python"
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

# Print all characters 
text = "python_devops_cloud_java"

for character in text:
    print(character)
    

# Print all characters 
# text = 123456789    
# for character in text: # TypeError: 'int' object is not iterable
#     print(character)

text = "python"
print(dir(text)) # All operations you can do with strings, we have __iter__ 

print("====================================")

prices = [1000,1500,2000,2500]
print(dir(prices)) # All operations you can do with lists, we have __iter__ 

print("====================================")

number = 123456789  
print(dir(number)) # All operations you can do with int, we do not have __iter__ 

print("====================================")

text = "python"
print("Length Of String: ",len(text))

prices = [1000,1500,2000,2500]
print("Number Of Prices: ",len(prices))

# Slicing 
text = "python"
print(text) 
print(text[::]) 
print(text[0:6:1]) 
print(text[0:3:1]) # pyt
print(text[0:3]) # pyt
print(text[1:3]) # yt
print(text[0:5:2]) # pto

print(text[-4:-1:1]) # tho
print(text[-4:-1:-1]) # 
print(text[-2:-6:-1]) # ohty

            #     0  1  2  3  4  5 (positive indexing)
            #     p  y  t  h  o  n
            #    -6 -5 -4 -3 -2 -1 (negative indexing)
            

# String Concatenation
s1 = "good"
s2 = "morning"
print(s1 + s2)

# Formatted String Literals (f-strings) 
age = 30
# print("My Age is "+age) # TypeError: can only concatenate str (not "int") to str
print(f"My Age is {age}")

# String Repetition 
laugh = "HaHa"
print(laugh)

hard_laugh = laugh * 10 
print(hard_laugh)

# String Immutability 
greet = "hello"
print(greet)
# Requirement is Print above as Hello 
print(greet[0])
# greet[0] = "H" # TypeError: 'str' object does not support item assignment
print(greet[0])

print("=" * 10)

# Example Of Mutable Type i.e List 
greet = ['h','i']
print(greet[0])
greet[0] = "H"
print(greet[0])
