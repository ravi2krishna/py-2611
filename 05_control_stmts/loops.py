# Looping Structures / Statements (Iteration Statements)

# while loop 

# while True: # this forms infinite loop 
#     print("Repeat..")
#     print("Repeat....")
#     print("Repeat...........")

# To terminate loop use control + c

count = 1
while count <=5 :
    print("Count is: ",count)
    count += 1
    
# use while, when we don't know number of Iterations/Repetitions in advance

# Real World Use Case 
# You found a lost phone, trying to break password
# tell me at what attempt, the phone will be unlocked ??

actual_pin = "2345"
user_given_pin = ""

while user_given_pin != actual_pin:
    user_given_pin = input("Enter PIN: ")
print("Phone Unlocked")


# for loop 
prices_of_products = [1000,1500,2000,2500,3000,3500,5000,10000]

# Some Offer is Running -> Provide a discount of 250 on each product 

# if we don't know for loop, we need to do manually 
print(prices_of_products)

# In Lists We have index(position), which starts from zero and keeps going on 
print(prices_of_products[0])
print(prices_of_products[1])
print(prices_of_products[2])

# Prices After Applying discounts 
print(prices_of_products[0] - 250)
print(prices_of_products[1] - 250)
print(prices_of_products[2] - 250)

# say we have 10000 products
# print(prices_of_products[9999] - 250)

print("===============")

# for loop -> 10000 products
prices_of_products = [1000,1500,2000,2500,3000,3500,5000,10000]

# for variable in sequence:
#     statements 
print("=========== Prices Before Discount ===========")
for individual_product_price in prices_of_products:
    print(individual_product_price) 
    
print("=========== Prices After Discount ===========")
for individual_product_price in prices_of_products:
    print(individual_product_price - 250) 

print("===============")

# we have a collection of 10000 names like this
# Requirement is format all the names in lower case 
names = ["RAvi","jOHN","miKE","liNDA"]

for name in names:
    print(name)

# Requirement is format all the names in lower case     
for name in names:
    print(name.lower())