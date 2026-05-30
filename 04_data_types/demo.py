# Data Types 

# Numeric Types 

data = 10
print(type(data))

data = -10
print(type(data))

data = 10.5
print(type(data))

data = -10.5
print(type(data))

# complex -> a + ib (maths)
# data = 3 + i5 # Error
# print(type(data))

# complex -> a + bj (python)
data = 3 + 5j
print(type(data))

data = True
print(type(data))

data = False
print(type(data))

data = None
print(type(data))

data = "python"
print(type(data))

# Complex Data Types 

# Lists
data = [1,2,3,4,5]
print(type(data))

# Tuples
data = (1,2,3,4,5)
print(type(data))

# sets
data = {1,2,3,4,5}
print(type(data))

# Dictionaries
data = {"sid":101,"name":"ravi","course":"python"}
print(type(data))

# Custom Data Type For Student 
class Student:
    student_id = 101
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    student_contact = 9999999999
    student_gpa = 9.3
    student_enrolled_courses = ["python","ai","cloud"]
    
data = Student() # Object Creation 
print(type(data))
print(data)
print(data.student_name)

# Type Conversion / Implicit Conversion [Automatic]
n1 = 10 # int
n2 = 5.5 # float
sum = n1 + n2 
print(sum)
print(type(sum))

# Type Casting / Explicit Conversion [Manual]
price = 1125.195 # float 
print(price)
print(type(price))

# round_off_price = data_type(variable_name)
round_off_price = int(price)
print(round_off_price)
print(type(round_off_price))


# Some User in a web site was filling some form (text boxes) 
# --> Behind the scenes these inputs are strings

rating = "4"
print(type(rating))

# if rating >= 4: # TypeError: '>=' not supported between instances of 'str' and 'int'
rating = int(rating)
if rating >= 4:    
    print("Positive Feedback") 
else:
    print("Negative Feedback")
    


