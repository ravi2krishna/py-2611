# Variables

# Assign Data (Store Data)
student_name = "Ravi" # String
student_age = 25 # int 
student_gpa = 9.5 # float 
student_passed = True # boolean 
STUDENT_AADHAR_ID = None # NoneType (None indicates absence of value)

# Retrieve Data (Fetch / Get Data)
print(student_name)
print(student_age)
print(student_gpa)
print(student_passed)
print(STUDENT_AADHAR_ID)

# Concatenation: Joining / Combining Strings Using + Operator      
print("=========== Student Information ===========")
# print("Student Name: Krishna") # Static / Hard Coding 
print("Student Name: " + student_name) # Dynamic 
# print("Student Age: " + student_age) # TypeError: can only concatenate str (not "int") to str
print("Student Age: ", student_age)
print("Student GPA: ", student_gpa)
print("Student Passed: ", student_passed)
print("Student AADHAR ID: ", STUDENT_AADHAR_ID)
print("=========== Student Information ===========")

# type() - Used to tell data type of a variable 
type(student_name)
print(type(student_name))
print(type(student_age))
print(type(student_gpa))
print(type(student_passed))
print(type(STUDENT_AADHAR_ID))

print("==========================")

# id() - Used to tell Memory Address of a variable 
id(student_name)
print(id(student_name))
print(id(student_age))
print(id(student_gpa))
print(id(student_passed))
print(id(STUDENT_AADHAR_ID))

print("==========================")

# Python Memory Model 
value_X = 10
print(id(value_X))

value_Y = 100
print(id(value_Y))

value_Z = 10
print(id(value_Z))
