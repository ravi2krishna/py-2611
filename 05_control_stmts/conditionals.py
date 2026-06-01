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