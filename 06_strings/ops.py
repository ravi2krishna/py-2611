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
    

# Simulate Phone ISD Scenario 
# https://us1.discourse-cdn.com/flex016/uploads/weweb/original/2X/d/dbe25afb4aeb05640347e2f7c1b7ae532ebb28f2.png
# https://www.businessbloomer.com/wp-content/uploads/2014/11/woocommerce-add-coupon-automatically-to-cart-if-product.png

# startswith() used to check if a string starts with a specific substring
# endswith() used to check if a string ends with a specific substring

contact_number = input("Enter Contact Number Starting With ISD Code: ")
print(f"India Number ? ",contact_number.startswith("+91"))

if contact_number.startswith("+91"):
    print("Calling India - Charged In Rupees")
elif contact_number.startswith("+33"):
    print("Calling France - Charged In Euros")
elif contact_number.startswith("+1"):
    print("Calling USA - Charged In Dollars")
else:
    print("Invalid Number - Only India, France & USA Numbers Allowed")
    
# Simulate Email Synchronization 
# endwith() method returns True if the string ends with the specified value, otherwise False.
source_email = input("Enter Source Email ID: ")
destination_email = input("Enter Destination Email ID: ")

if source_email.endswith("@gmail.com") and destination_email.endswith("@gmail.com"):
    print("Email Backup Process Started")
else:
    print("Email Backup Process Failed - Source and Destination Didn't Match")

# Simulate File Types Processing In Websites like image upload  
file_type = input("Enter You File Name Along with Extension: ")

if file_type.endswith(".jpeg") or file_type.endswith(".png") or file_type.endswith(".svg"):
    print("Processing Image File")
    
elif file_type.endswith(".pdf") or file_type.endswith(".doc") or file_type.endswith(".txt"):
    print("Processing Document File")

elif file_type.endswith(".mp4") or file_type.endswith(".avi") or file_type.endswith(".mpeg"):
    print("Processing Video File")

else:
    print("Unknown Format")
    

# Simulate Data Operations Work: CSV Data from a file and perform some operations 
# https://www.datablist.com/learn_images/csv/google_sheet_csv.png
# https://www.slashgear.com/img/gallery/csv-files-explained-what-they-are-and-how-to-open-them/what-are-csv-files-1699455969.jpg
# Name,Email,Age,City,Job_Role
# emp_data = "John,john@apple.com,30,Hyderabad,Developer"
# Requirement: Display Employee Name & Job Role 

emp_data = "John,john@apple.com,30,Hyderabad,Developer"

emp_name = emp_data[0]
print("Employee Name: ",emp_name)

emp_name = emp_data[0:4]
print("Employee Name: ",emp_name)

emp_data = "Michael,michael@apple.com,30,Hyderabad,Developer"
emp_name = emp_data[0:7]
print("Employee Name: ",emp_name)

# Using Above Approach, we have hard coded logic, which is not good 
# split() method breaks a string into a list of substrings based on a specified delimiter. 
# It is a built-in string manipulation tool commonly used for data parsing, 
# processing CSV files, and handling user inputs.
emp_data = "Michael,michael@apple.com,30,Hyderabad,Developer"
data_splitted = emp_data.split()
print(data_splitted)

emp_data = "Michael michael@apple.com 30 Hyderabad Developer" # splits data by space default
data_splitted = emp_data.split()
print(data_splitted)

emp_data = "Michael-michael@apple.com-30-Hyderabad-Developer"
data_splitted = emp_data.split("-")
print(data_splitted)

emp_data = "Michael,michael@apple.com,30,Hyderabad,Developer"
data_splitted = emp_data.split(",")
print(data_splitted)
emp_name = data_splitted[0]
emp_role = data_splitted[-1]
print("Employee Name: ",emp_name)
print("Employee Role: ",emp_role)

emp_data = "bignameeeeeeeeeeeeeeeeee,michael@apple.com,30,Hyderabad,Developer"
data_splitted = emp_data.split(",")
print(data_splitted)
print("Employee Name: ",data_splitted[0])
print("Employee Role: ",data_splitted[-1])


# Simulate Amazon Order Email / SMS / OTP Confirmation Template 
order_template = "Hello, Your Order with order_id has been shipped"
order_ids = "AMAZON-ID-1010029202,AMAZON-ID-8090029202,AMAZON-ID-9090029202,AMAZON-ID-7080029202"

# Hello, Your Order with AMAZON-ID-1010029202 has been shipped
# Hello, Your Order with AMAZON-ID-8090029202 has been shipped
# Hello, Your Order with AMAZON-ID-9090029202 has been shipped
# Hello, Your Order with AMAZON-ID-7080029202 has been shipped

order_ids_extracted = order_ids.split(",")
print("All order ID's :",order_ids_extracted)

for order_id in order_ids_extracted:
    # replace() method is used to swap out a specific substring for a new one within a string
    # replace(old,new)
    send_email = order_template.replace("order_id",order_id)
    print(send_email)