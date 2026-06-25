# Working With CSV Files 

# Read Data From CSV File 
# Read Whole Data 
with open("14_file_manage/students.csv","r") as file_data:
    print(file_data.read())
    
print("=" * 50)

# Customer Requirement: Fetch me all the students from Hyderabad 
# Now all above data is One String 

# Read Data From CSV File Recommended Way 
import csv 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        print(row)
    
print("=" * 50)

# Customer Requirement: Fetch me all the students from Hyderabad
# Assume We Have 10K -> 100k Students Records In CSV File 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        print(row)
    
print("=" * 50)

# Customer Requirement: Fetch me all the students from Hyderabad
# Assume We Have 10K -> 100k Students Records In CSV File 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row)
        if row[-1] == "Hyderabad":
            print(row)  
    
print("=" * 50)


# Customer Requirement: Fetch me all the students from tcs and Hyderabad
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row)
        if row[-1] == "Hyderabad" and row[1].endswith("@tcs.com"):
            print(row)  
    
print("=" * 50)


# NOW DATA SETS ARE CHANGED
# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row)
        if row[-1] == "Hyderabad":
            print(row)  
    
print("=" * 50) # Failed 

# NOW DATA SETS ARE CHANGED
# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)  
    for row in csv_reader:
        print(row) # Data is in Dictionary Format
        # {'name': 'Hari', 'mobile': '9889032187', 'address': 'Jaipur', 'email': 'hari193@outlook.com'}
        
        # Earlier Data was in List Format when we used reader()
        # ['Naveen', 'naveen409@tcs.com', '9806720153', 'Hyderabad']
    
print("=" * 50)

# NOW DATA SETS ARE CHANGED
# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)  
    for row in csv_reader:
        if row['address'] == "Hyderabad":
            print(row)  
    
print("=" * 50)

# NOW DATA SETS ARE CHANGED
# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)  
    for row in csv_reader:
        if row['address'] == "Hyderabad":
            print(row)  
    
print("=" * 50)

# Create and Write Data To CSV File
with open("14_file_manage/emp.csv","w") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name', 'email', 'mobile', 'address'])
    csv_writer.writerows([
        ['Lokesh', 'lokesh489@gmail.com', '9879744557', 'Hyderabad'],
        ['Santosh', 'santosh579@outlook.com', '9718726887', 'Hyderabad'],
        ['Naveen', 'naveen409@tcs.com', '9806720153', 'Hyderabad']
    ])

print("=" * 50)

# Create and Write Data To CSV File
fieldnames = ['name', 'email', 'mobile', 'address']
with open("14_file_manage/new.csv","w") as file_data:
    # csv_writer = csv.DictWriter(file_data) # TypeError: DictWriter.__init__() missing 1 required positional argument: 'fieldnames'
    csv_writer = csv.DictWriter(file_data,fieldnames)
    
    # Write the column headers
    csv_writer.writeheader()
    
    csv_writer.writerow({'name': 'Mahesh', 'mobile': '9969450859', 'address': 'Hyderabad', 'email': 'mahesh381@tcs.com'})
    csv_writer.writerows([
        {'name': 'Lokesh', 'email': 'lokesh489@gmail.com', 'mobile': '9879744557', 'address': 'Hyderabad'},
        {'name': 'Santosh', 'email': 'santosh579@outlook.com', 'mobile': '9718726887', 'address': 'Hyderabad'},
        {'name': 'Naveen', 'email': 'naveen409@tcs.com', 'mobile': '9806720153', 'address': 'Hyderabad'}
    ])