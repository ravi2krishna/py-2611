# Branching Structures / Statements (Jump Statements)

for num in range(1,11,1):
    print(num)
    
# Stop when num is 5 
# break: helps you exit the loops  
for num in range(1,11,1):
    if num == 5:
        break
    print(num)
    
    
# skip 5th number 
# continue: helps you skip the current iteration 
for num in range(1,11,1):
    if num == 5:
        continue
    print(num)
    
# Real World Use Cases
# ATM PIN Validation - like 3 unsuccessful attempts lock Card / Account 
# Finding specific product out of multiple products 

# pass: acts as a placeholder, does nothing 
# Requirement - To Perform Some Operations in the Future 
# When Salary is above 25000, we want to do something 
# emp_salary = 15000

emp_salary = 15000
if emp_salary > 25000:
    print("Something i will do in future")
    
emp_salary = 15000
if emp_salary > 25000:
    pass # _______

# Other operations to work on
print("Working With Next Functionalities")

# After 6 months 
# When Salary is above 25000, we want to do something 
# something is promote to junior engineer 
emp_salary = 30000
if emp_salary > 25000:
    print("Trainee Promoted To Junior Engineer")
    
# When Working With OOP 
class Employee:
    pass 

class Manager:
    pass 

class Developer:
    name = "John"
    location = "Hyderabad" 