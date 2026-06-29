# Exception Handling 

# When No Errors --> Nothing To Handle 

print("Program Execution Started")

num1 = 10
num2 = 5

print("Result: ", num1/num2)

print("Program Execution Completed")

print("=" * 50)

# # When Errors --> abruptly "STOPS" the program execution

# print("Program Execution Started")

# num1 = 10
# num2 = "5"

# print("Result: ", num1/num2) # TypeError: unsupported operand type(s) for /: 'int' and 'str'

# print("Program Execution Completed")

# print("=" * 50)

# When Errors --> Developers Handling Exceptions 

print("Program Execution Started")

num1 = 10
num2 = "5"

try:
    print("Result: ", num1/num2) # TypeError: unsupported operand type(s) for /: 'int' and 'str'
except:
    print("WARNING! Don't Divide Numbers With Strings")

print("Program Execution Completed")

print("=" * 50)

# When No Errors --> Developers Handling Exceptions 

print("Program Execution Started")

num1 = 10
num2 = 5

try:
    print("Result: ", num1/num2) # TypeError: unsupported operand type(s) for /: 'int' and 'str'
except:
    print("WARNING! Don't Divide Numbers With Strings")

print("Program Execution Completed")

print("=" * 50)


# # When Errors --> Python Handling Exceptions 

# print("Program Execution Started")

# num1 = 10
# num2 = 0

# print("Result: ", num1/num2) # ZeroDivisionError: division by zero

# print("WARNING! Don't Divide Numbers With Strings")

# print("Program Execution Completed")

# print("=" * 50)

# When Errors --> Developers Handling Exceptions 

print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print("Result: ", num1/num2) 
except:
    print("WARNING! Don't Divide Numbers With Zero -  https://en.wikipedia.org/wiki/Division_by_zero")

print("Program Execution Completed")

print("=" * 50)

# When Multiple Errors Occur 
# data = [1,2,'three',0,4]
# data = [1,2,0,4]
data = [1,2,4]

for num in data:
    print(1/num)
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero

print("=" * 50)

# When Multiple Errors Occur  --> Developers Handling Exceptions 

print("Program Execution Started")

data = [1,2,'three',0,4]
for num in data:
    try:
        print(1/num)
        # TypeError: unsupported operand type(s) for /: 'int' and 'str'
        # ZeroDivisionError: division by zero
    except:
        print("OOPS!!! Something Went Wrong")

print("Program Execution Completed")

print("=" * 50)

# When Multiple Errors Occur Use Multiple except blocks  --> Developers Handling Exceptions 

print("Program Execution Started")

data = [1,2,'three',0,4]
for num in data:
    try:
        print(1/num)
        # TypeError: unsupported operand type(s) for /: 'int' and 'str'
        # ZeroDivisionError: division by zero
    except TypeError:
        print("OOPS!!! Don't Divide Numbers With Strings")

    except ZeroDivisionError:
        print("OOPS! Don't Divide Numbers With Zero -  https://en.wikipedia.org/wiki/Division_by_zero")
    
print("Program Execution Completed")

print("=" * 50)

# When Errors occur else scenario --> Developers Handling Exceptions 

print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print("Result: ", num1/num2) 
except:
    print("WARNING! Don't Divide Numbers With Zero -  https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Was Successful")

print("Program Execution Completed")

print("=" * 50)

# When Errors occur else scenario --> Developers Handling Exceptions 

print("Program Execution Started")

num1 = 10
num2 = 5

try:
    print("Result: ", num1/num2) # Verify Login Credentials 
except:
    print("WARNING! Don't Divide Numbers With Zero -  https://en.wikipedia.org/wiki/Division_by_zero")
else: 
    print("Calculation Was Successful") # Then Only Check For OTP

print("Program Execution Completed")

print("=" * 50)

# When Errors occur finally scenario --> Developers Handling Exceptions 

print("Program Execution Started")

num1 = 10
num2 = 5

try:
    print("Result: ", num1/num2) # Verify Login Credentials 
except:
    print("WARNING! Don't Divide Numbers With Zero -  https://en.wikipedia.org/wiki/Division_by_zero")
else: 
    print("Calculation Was Successful") # Then Only Check For OTP
finally:
    print("Closing All Database Connections & File Streams")

print("Program Execution Completed")

print("=" * 50)

# When Errors occur finally scenario --> Developers Handling Exceptions 

print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print("Result: ", num1/num2) # Verify Login Credentials 
except:
    print("WARNING! Don't Divide Numbers With Zero -  https://en.wikipedia.org/wiki/Division_by_zero")
else: 
    print("Calculation Was Successful") # Then Only Check For OTP
finally:
    print("Closing All Database Connections & File Streams")

print("Program Execution Completed")

print("=" * 50)

# Custom Exceptions 
age = int(input("Enter Age: "))
if age < 18:
    print("You Cannot Vote")
else:
    print("You Can Vote")
    
print("=" * 50)

# # Custom Exceptions Specific to your program 
# class UnderAgeError(Exception):
#     pass 

# age = int(input("Enter Age: "))
# if age < 18:
#     # print("You Cannot Vote")
#     raise UnderAgeError
# else:
#     print("You Can Vote")
    
# print("=" * 50)

# # Custom Exceptions Specific to your program 
# class UnderAgeError(Exception):
#     pass 

# age = int(input("Enter Age: "))
# if age < 18:
#     # print("You Cannot Vote")
#     raise UnderAgeError("Below 18 Cannot Vote")
# else:
#     print("You Can Vote")
    
# print("=" * 50)

# Custom Exceptions Specific to your program 
class UnderAgeError(Exception):
    pass 

age = int(input("Enter Age: "))
try:
    if age < 18:
    # print("You Cannot Vote")
        raise UnderAgeError("Below 18 Cannot Vote")
except UnderAgeError:
    print("You are not 18 Yet!!!!!")
else:
    print("You Can Vote")
    
print("=" * 50)