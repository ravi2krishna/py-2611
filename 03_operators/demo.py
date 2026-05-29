# Operators 

# Arithmetic Operators
num1 = 10
num2 = 5

print("Sum Of Numbers: ",num1+num2)
print("Difference Of Numbers: ",num1-num2)
print("Product Of Numbers: ",num1*num2)
print("Division Of Numbers: ",num1/num2)
print("Modulus Of Numbers: ",num1%num2)

print("Normal Division: ",3/2)
print("Floor Division: ",3//2)
print("Exponentiation: ",3 ** 2) # 3 ^ 2

print("=======================")

# Compound Assignment Operators

num = 10
num = num + 5 # long form 
print(num)

num = 10
num += 5 # short form 
print(num)

# Increment & Decrement increase or decrease a variable's value by one
# used in loops in our upcoming sessions
count = 0
print(count)
# count++ # SyntaxError: invalid syntax
count += 1
print(count)
count += 1
print(count)
count += 1
print(count)

count = 10
print(count)
count -= 1
print(count)
count -= 1
print(count)

print("=======================")

# Comparison Operators
num1 = 3
num2 = 2

print(num1 == num2) 
print(num1 != num2) 
print(num1 > num2) 

print("=======================")

# Logical Operators
num1 = 1
num2 = 2
num3 = 3
num4 = 4

print (num1 > num2 and num3 > num4) # F and F -> F
print (num1 < num2 and num3 > num4) # T and F -> F
print (num1 < num2 and num3 < num4) # T and T -> T

print (num1 > num2 or num3 > num4) # F or F -> F
print (num1 < num2 or num3 > num4) # T or F -> T
print (num1 < num2 or num3 < num4) # T and T -> T

print(num1 > num2) # F
print(not num1 > num2) # T

print("=======================")

# Membership Operators
sentence = "python is interpreted language"
find_word = "java"
status = find_word in sentence
print(status)

sentence = "python is interpreted language"
find_word = "python"
status = find_word in sentence
print(status)

# List Data Type -> [] 
employee_ids = ["101101","202101","301101","901101"]
find_by_emp_id = "701101"
status = find_by_emp_id in employee_ids
print(status)

status = find_by_emp_id not in employee_ids
print(status)

