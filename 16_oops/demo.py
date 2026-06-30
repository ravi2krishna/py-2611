# OOP - Object Oriented Programming 

# Class - Blue Print 

class Student:
    
    # Student Has Something - Characteristics / Properties (VARIABLES)
    student_name = "ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions (METHODS)
    def student_studies():
        print("Student Is Studying Python")
        
# To Use this class, object is required 
student_object = Student()

print("Student Name: ",student_object.student_name)
print("Student Email: ",student_object.student_email)

# student_object.student_studies() # TypeError: Student.student_studies() takes 0 positional arguments but 1 was given

print("=" * 50)

# Class - Blue Print 

class Student:
    
    # Student Has Something - Characteristics / Properties (VARIABLES)
    student_name = "ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions (METHODS)
    def student_studies(self): # passed "self" nothing but object reference 
        print("Student Is Studying Python")
        
# To Use this class, object is required 
student_object = Student()

print("Student Name: ",student_object.student_name)
print("Student Email: ",student_object.student_email)

student_object.student_studies() 

print("=" * 50)

# Class - Blue Print 

class Student:
    
    # Student Has Something - Characteristics / Properties (VARIABLES)
    student_name = "ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions (METHODS)
    def student_studies(self): # passed "self" nothing but object reference 
        print("Student Is Studying Python")
        print("Student Name: ",self.student_name) # Recommended
        print("Student Email: ",student_object.student_email) # Not Recommended
        
# To Use this class, object is required 
student_object = Student()

student_object.student_studies() 

print("=" * 50)

# Class - Blue Print 

class Student:
    
    # Student Has Something - Characteristics / Properties (VARIABLES)
    student_name = "ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions (METHODS)
    def student_studies(self): # passed "self" nothing but object reference 
        print("Student Is Studying Python")
        print("Student Name: ",self.student_name) # Recommended
        print("Student Email: ",self.student_email) # Not Recommended
        
# To Use this class, object is required 
student_object = Student()

student_object.student_studies() 

print("=" * 50)

# Working With Multiple Objects 

class Student:
    
    # Student Has Something - Characteristics / Properties (VARIABLES)
    student_name = "ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions (METHODS)
    def student_studies(self): # passed "self" nothing but object reference 
        print("Student Is Studying Python")
        print("Student Name: ",self.student_name) # Recommended
        print("Student Email: ",self.student_email) # Not Recommended
        
# To Use this class, object is required 
student_ravi = Student()
student_ravi.student_studies() 

student_john = Student()
student_john.student_studies() 

student_mike = Student()
student_mike.student_studies() 

print("=" * 50)

# Working With Multiple Objects Using Constructor i.e __init__() method

class Student:
    
    # Student Has Something - Characteristics / Properties (VARIABLES)
    # student_name = "ravi"
    # student_email = "ravi2krishna@gmail.com"
    
    
    # Constructor i.e __init__() method
    def __init__(self,student_name,student_email):
        print("Constructor Called")
        self.student_name = student_name
        self.student_email = student_email
        
    
    # Student Does Something - Behaviors / Actions (METHODS)
    def student_studies(self): # passed "self" nothing but object reference 
        print("Student Is Studying Python")
        print("Student Name: ",self.student_name) # Recommended
        print("Student Email: ",self.student_email) # Not Recommended
        
# To Use this class, object is required 
# student_ravi = Student()
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_studies() 

student_john = Student("john","john@gmail.com")
student_john.student_studies() 

student_mike = Student("mike","mike@gmail.com")
student_mike.student_studies() 

print("=" * 50)