# String Methods 

# Simulate Gmail Functionality 

#     RaVI2KRiShNA      -> ravi2krishna@gmail.com 

email = input("Enter Email ID: ")
print("Original Email ID Given: "+email)

# lower() - Converts a string to lowercase
transformed_email = email.lower()
print("Transformed Email ID is: "+transformed_email)

# strip(): Removes spaces from both ends i.e left side and right side 
# lstrip(): Removes spaces from left side 
# rstrip(): Removes spaces from right side 

transformed_email = transformed_email.strip()
print("Transformed Email ID is: "+transformed_email)

# Add domain like @gmail.com using concatenation 
domain = "@gmail.com"
transformed_email = transformed_email + domain
print("Transformed Email ID is: "+transformed_email)


# Simulate PAN Functionality 
# https://www.pan.utiitsl.com/
# PAN Card is 10 Character Alphabets & Numbers in Upper Case - ampOL8891W -> @MPOL8891W

pan_card_id = input("Enter PAN Card ID For Correction: ")
print("Original PAN: "+pan_card_id)

# isalnum(): Returns True if all characters are letters or numbers, otherwise False 
# isalpha(): Returns True if all characters are letters, otherwise False 
# isdigit(): Returns True if all characters are numbers, otherwise False 

print("Is it alpha numeric:", pan_card_id.isalnum())
print("Is it alpha numeric:","AMPOL8891W".isalnum())
print("Is OTP numeric:","AMPOL8891W".isdigit())
print("Is OTP numeric:","123456".isdigit())

if pan_card_id.isalnum() and len(pan_card_id) == 10:
    print("Original PAN Card ID: "+pan_card_id)
    print(f"Given PAN {pan_card_id} is VALID and Transforming")
    # upper() - Converts a string to uppercase
    print("Transformed PAN: "+pan_card_id.upper())
else:
    print(f"Given PAN {pan_card_id} is INVALID")
    

