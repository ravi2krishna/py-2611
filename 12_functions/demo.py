# Functional Programming 

# Without Functions

# User One Wants to do calculations with below values
num1 = 10
num2 = 5

# Math Operations
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 10)

# User Two Wants to do calculations with below values
num1 = 20
num2 = 5

# Math Operations
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 10)

# User Three Wants to do calculations with below values
num1 = 200
num2 = 50

# Math Operations
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 10)


# With Functions
def math_ops():
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)

# User One Wants to do calculations with below values
num1 = 10
num2 = 5
math_ops()

print("=" * 10)

# User Two Wants to do calculations with below values
num1 = 20
num2 = 5
math_ops()

print("=" * 10)

# User Three Wants to do calculations with below values
num1 = 200
num2 = 50
math_ops()

print("=" * 10)

# math_ops(1000,500) # TypeError: math_ops() takes 0 positional arguments but 2 were given


# With Functions and Parameters 
def math_ops(num1,num2):
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)
    
# math_ops() # TypeError: math_ops() missing 2 required positional arguments: 'num1' and 'num2'
math_ops(10,5) # User One Wants to do calculations with below values
math_ops(20,5) # User Two Wants to do calculations with below values
math_ops(200,50) # User Three Wants to do calculations with below values

print("=" * 10)

# Positional Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")
    
employee_info("Hyderabad","ravi","ravi2krishna@gmail.com") # Order Matters leading to errors or unexpected behavior

print("=" * 10)

employee_info("ravi","ravi2krishna@gmail.com","Hyderabad")  

print("=" * 10)

# Keyword Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")
    
employee_info("Hyderabad","ravi","ravi2krishna@gmail.com") # Positional 

print("=" * 10)

employee_info(emp_location="Hyderabad",emp_name="ravi",emp_email="ravi2krishna@gmail.com") # Keyword 

print("=" * 10)

# Without Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")

employee_info(emp_location="Hyderabad",emp_name="ravi",emp_email="ravi2krishna@gmail.com",org_name="TCS") # Keyword 
employee_info(emp_location="Bangalore",emp_name="krishna",emp_email="krishna@gmail.com",org_name="TCS") # Keyword 
employee_info(emp_location="Pune",emp_name="Sam",emp_email="sam@gmail.com",org_name="TCS") # Keyword 
# Similarly we have 20 other employees all working for TCS 
print("=" * 10)


# With Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name="TCS"):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")

employee_info(emp_location="Hyderabad",emp_name="ravi",emp_email="ravi2krishna@gmail.com") # Keyword 
employee_info(emp_location="Bangalore",emp_name="krishna",emp_email="krishna@gmail.com") # Keyword 
employee_info(emp_location="Pune",emp_name="Sam",emp_email="sam@gmail.com") # Keyword 
# Similarly we have 20 other employees all working for TCS 

# one special employee Mike is from IBM 
employee_info(emp_location="Delhi",emp_name="Mike",emp_email="mike@gmail.com",org_name="IBM") # Keyword 

print("=" * 10)

# # Placement Requirement: Default arguments
# def employee_info(emp_name,emp_email,emp_location,org_name="TCS",emp_mobile): # Non-default argument follows default argument
#     print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")


# Placement Requirement: Default arguments
def employee_info(emp_name,emp_email,emp_location,emp_mobile,org_name="TCS"): # Non-default argument follows default argument
    print(f"Hi {emp_name} your email is {emp_email}, your mobile number is{emp_mobile} and working for {org_name} at location {emp_location}")


# Placement Requirement: Default arguments
def employee_info(emp_name,emp_email,emp_location,org_name="TCS",emp_mobile="88888"): # Non-default argument follows default argument
    print(f"Hi {emp_name} your email is {emp_email}, your mobile number is{emp_mobile} and working for {org_name} at location {emp_location}")

print("=" * 50)

# Without Arbitrary Positional Arguments
def add_numbers_one(n1):
    print(n1)
    
def add_numbers_two(n1,n2):
    print(n1+n2)   
    
def add_numbers_three(n1,n2,n3):
    print(n1+n2+n3)     
    
add_numbers_one(10)
add_numbers_two(10,20)
add_numbers_three(10,20,30)
# add_numbers_three(10,20,30,40,50) # TypeError: add_numbers_three() takes 3 positional arguments but 5 were given

print("=" * 50)

# With Arbitrary Positional Arguments
def add_numbers(*numbers):
    print(numbers)
    
add_numbers(10)
add_numbers(10,20)
add_numbers(10,20,30)
add_numbers(10,20,30,40,50)

print("=" * 50)

def add_numbers(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    print(f"Total Sum is {sum}")

add_numbers(10)
add_numbers(10,20)
add_numbers(10,20,30)
add_numbers(10,20,30,40,50)

print("=" * 50)

def profile(*info):
    print(info)
    
profile("ravi","krishna")
profile("ravi","krishna","ravi@gmail.com")

print("=" * 50)

# Real World Use Case W.R.T Ecommerce Application (Amazon.in) Cart Functionality 
def cart_total_value(*products):
    total_cart_value = 0
    for product_price in products:
        total_cart_value += product_price
    print(f"Total Cart Value Is ₹ {total_cart_value}")
    
cart_total_value(34900,11299,2299)

print("=" * 50)

# Arbitrary Keyword Arguments
def profile(**info):
    print(info)
    
# profile("ravi","krishna") # TypeError: profile() takes 0 positional arguments but 2 were given
profile(first_name="Ravi")
profile(first_name="Ravi",last_name="krishna",email="ravi@gmail.com")

print("=" * 50)

def profile(**info):
    for data in info:
        print(data)

profile(first_name="Ravi",last_name="krishna",email="ravi@gmail.com")

print("=" * 50)

def profile(**info):
    for data in info:
        print(info[data])

profile(first_name="Ravi",last_name="krishna",email="ravi@gmail.com")

print("=" * 50)

# Real World Use Case -> jan=3000, feb=4500, mar=9000
# Requirement: Calculate Total Transaction Amount and Number Of Transactions Made
def bank_transactions(**transactions):
    print(transactions)
    total_transactions = 0
    number_of_transactions = 0
    for transaction in transactions:
        total_transactions += transactions[transaction]
        number_of_transactions += 1 
    print(f"Total transactions amount is {total_transactions} for {number_of_transactions} transactions")
    
bank_transactions(jan=3000, feb=4500, mar=9000)    
bank_transactions(jan=3000, feb=4500, mar=9000, apr=1000, may=2000, june=6000)

print("=" * 50)

# Without return keyword 
def add(a,b):
    a + b #  When you don't use a return, by default a function returns None 

add(10,20)
print(add(10,20))

print("=" * 50)

# Without return keyword and print
def add(a,b):
    print(a + b)

add(10,20)

print("=" * 50)

# def special_add(a,b):
#     print(add(10,20)+b) # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
    
# special_add(100,200) 

print("=" * 50)

# With return keyword
def add(a,b):
    return a + b

add(100,200)
print(add(100,200))

print("=" * 50)

def special_add(a,b):
    print(add(10,20)+b)

special_add(100,200) 

print("=" * 50)

# Function Composition: function calling another function
def add(a,b):
    return a + b

def sub(c,d,e): # add c & d, then minus e --> c + d - e
    return add(c,d) - e 

print(sub(3,4,5)) # return add(c,d) - e --> return 7 - e --> return 7 - 5 = 2

print("=" * 50)    
    
# return - make sure it's the last part of statement to be executed
def add(a,b):
    print("Calculation Started")
    return a + b
    print("Calculation Completed") # Code is structurally unreachable

print(add(500,500))

print("=" * 50) 

a = 10
a = 20 
print(a) 

print("=" * 50) 

# If you have multiple return statements, first return will be considered
def math_ops(num1,num2):
    return num1 + num2
    return num1 * num2
    return num1 / num2

print(math_ops(10,20))

print("=" * 50) 

# multiple returns are present, and used with conditionals
def math_ops(num1,num2,operator):
    if operator == "+":
        return num1 + num2 
    elif operator == "-":
        return num1 - num2 
    elif operator == "*":
        return num1 * num2 
    else:
        return "Invalid Operator"
    
print(math_ops(200,100,"+"))
print(math_ops(200,100,"*"))
print(math_ops(200,100,"@"))

print("=" * 50) 

# Local Scope
def add():
    local_a = 10 # local variable - declared "inside the function" 
    local_b = 20 # local variable - declared "inside the function" 
    print(local_a)
    print(local_b)
    
add()

# print(local_a) # name 'local_a' is not defined

print("=" * 50) 

# Parameters we are passing to the functions, are also local variables        
def add(local_a,local_b): # local variables - local_a,local_b
    print(local_a)
    print(local_b)
    
add(100,200)
    
# print(local_a) # name 'local_a' is not defined    
    
print("=" * 50) 

# Global Scope
global_a = 100 # global variable - declared "outside the function" 

def add():
    local_a = 10 # local variable - declared "inside the function" 
    local_b = 20 # local variable - declared "inside the function" 
    print(local_a)
    print(local_b)
    print(global_a) # global variable - accessed "inside the function" 

add()
print(global_a) # global variable - accessed "outside the function"    

print("=" * 50) 

# Name Conflict 
global_a = 100 # global variable - declared "outside the function" 
def add(local_a,local_b,global_a): # local variables - local_a,local_b, global_a
    print(local_a)
    print(local_b)
    print(global_a)

add(1,2,3)    

print("=" * 50) 

# Name Conflict & Access Global too
global_a = 100 # global variable - declared "outside the function" 
def add(local_a,local_b,global_a): # local variables - local_a,local_b, global_a
    print(local_a)
    print(local_b)
    print(global_a)
    print(globals()['global_a'])

add(1,2,3)    

print("=" * 50) 

# global variables outside the function 
count = 0
print(count)
count += 1
print(count)

print("=" * 50) 

# global variables inside the function 
count = 0
print(count)

def increment():
    global count
    count += 1 # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    print(count)

increment()

print("=" * 50) 

# Built in functions 
# print()
# id()
# type()
# dir()
# len()

# Without Lambda i.e Regular Function 
def add(a,b):
    return a+b 
print(add(40,50))

print("=" * 50) 

# With Lambda, Same above operation
# lambda arguments:expression 

lambda a,b:a+b # lambda function i.e One Liner Function  
print((lambda a,b:a+b)(60,70))

print("=" * 50) 

# Without Lambda i.e Regular Function 
def is_even_num(num):
    if num % 2 == 0:
        return True 
    else:
        return False 
print(is_even_num(11))
print(is_even_num(10))

print("=" * 50) 

# With Lambda, Same above operation
# lambda arguments:expression 

lambda num:num % 2 == 0 # lambda function i.e One Liner Function  
print((lambda num:num % 2 == 0)(9))
print((lambda num:num % 2 == 0)(8))

print("=" * 50) 

# Without Lambda i.e Regular Function 
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")
employee_info(emp_location="Hyderabad",emp_name="ravi",emp_email="ravi2krishna@gmail.com")

print("=" * 50) 

# With Lambda, Same above operation
# lambda arguments:expression 
lambda emp_name,emp_email,emp_location:print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")
print((lambda emp_name,emp_email,emp_location:print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}"))(emp_location="Hyderabad",emp_name="ravi",emp_email="ravi2krishna@gmail.com"))
