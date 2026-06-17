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
