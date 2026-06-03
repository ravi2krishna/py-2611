# Nested Conditionals 

# inner condition is only checked if the outer condition is true. 

if True:
    print("Check")
if True:
    print("This is NOT Nested Condition")
    
if True: # Outer Condition 
    print("Outer Check")
    if True: # Inner Condition 
        print("Inner Check")
        
    
if False: # Outer Condition 
    print("Outer Check")
    if True: # Inner Condition 
        print("Inner Check")
    
# Nested Conditional Use Case 
# Voting App
name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))

if age >= 18:
    has_id = input("Do You Hav ID (yes/no): ")
    if has_id == "yes":
        print(f"{name} You Can Vote")
    else:
        print(f"{name} You Cannot Vote Without ID")
else:
    print(f"{name} You Cannot Vote as you are still {age} years only")
    
# Other Real World Examples Include 
# ATM Pin & Withdraw functionality 
# Login Authentication(username & password) & Login Authorization (OTP)
# Work On Above Tasks 