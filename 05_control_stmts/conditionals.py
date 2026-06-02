# if condition

if 5 > 2:
    print("Yes 5 > 2 is Correct")

if 5 < 2:
    print("Yes 5 < 2 is Correct")    

num = 10
if num > 0:
    print("Given Number is Positive")
    
num = -10
if num > 0:
    print("Given Number is Positive")
    
    
num = -10
if num > 0:
    print("Given Number is Positive")
if num < 0:
    print("Given Number is Negative")
    
# if else condition    
num = 10
if num > 0:
    print("Given Number is Positive")
else:
    print("Given Number is Negative")


# without input() - user input is hardcoded
name = "Ravi"
print(name)

# input(): reads the input from user and stores the value as String 
name = input("Enter Your Name: ")
print(name)


num = input("Enter Number: ")
num = int(num)
if num > 0: # TypeError: '>' not supported between instances of 'str' and 'int'
    print("Given Number is Positive")
else:
    print("Given Number is Negative")
    
# Read Some Name
name = input("Enter Your Name: ")
print(name)
print("Welcome: "+name) # Concatenation 
print("Welcome: ",name) # Comma Operator
print("Welcome {name}") # No Interpolation
print(f"Welcome {name}") # With Interpolation
 
num = input("Enter Number: ")
num = int(num)
if num > 0: # TypeError: '>' not supported between instances of 'str' and 'int'
    print(f"Given Number {num} is Positive")
else:
    print(f"Given Number {num} is Negative")
    
print("=========================")

# Real World Use Case For if-else 
# Voting App
name = input("Enter Your Name: ")
# age = int(age)
age = int(input("Enter Your Age: "))

if age >= 18:
    print(f"{name} You Can Vote")
else:
    print(f"{name} You Cannot Vote as you are still {age} years only")


# Conditional Expression 
age = int(input("Enter Your Age: "))
# value_if_true if condition else value_if_false 
status = "You Can Vote" if age >= 18 else "You Cannot Vote" 
print(status)

# Only two checks if-else 
marks = int(input("Enter Your Marks: "))
if marks >= 35:
    print("Passed")
else:
    print("Failed")
    
# Multiple Checks to be done
# Check for grades according to marks 
marks = int(input("Enter Your Marks: "))
if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
elif marks >= 50:
    print("D Grade")
elif marks >= 35:
    print("E Grade")
else:
    print("Failed")
    
# match case 
choices = "1 - Burger > 2 - Pizza > 3 - Pasta > 4 - Biryani"
print(choices)
food_item = int(input("Enter Your Choice: "))
match food_item:
    case 1:
        print("Ordered Burger")
    case 2:
        print("Ordered Pizza")
    case 2:
        print("Ordered Pasta")
    case 4:
        print("Ordered Biryani")
    case _:
        print("Invalid Choice")
        

atm_menu = "1 - Deposit Amount > 2 - Withdraw Amount > 3 - Check Balance > 4 - Exit"
print(atm_menu)
user_choice = int(input("Enter Your Choice: "))
match user_choice:
    case 1:
        print("Deposited Amount")
    case 2:
        print("Withdrawn Amount")
    case 3:
        print("Checked Balance")
    case 4:
        print("Remove Card")
    case _:
        print("Invalid Choice")