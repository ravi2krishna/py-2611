# Student Management System

# Menu Based System -> In Future if you learn html, css, js etc, replace menus with 
# UI Elements like Buttons 

# System Setup -> READ ONLY (Tuple)
# System_info = () # Not Recommended 
SYSTEM_INFO = ("Digital Tech","Student Management System","v1")

# Admin Info -> READ ONLY (Tuple)
ADMIN_INFO = ("9999999999","admin@digital.com")

# Display System Info 
print("=" * 50)
print(f"        Welcome To {SYSTEM_INFO[0]}")
print(f"        Software {SYSTEM_INFO[1]} - {SYSTEM_INFO[-1]}")
print("=" * 50)

# Core Functionalities (CRUD)
# Add Student -> ID, Name, Scores, Skills
# Add Student -> ID(only one), Name(only one), Scores(Multiple), Skills(Multiple)
# Whole System -> Multiple Students -> Which Data Structure is appropriate ?

# Whole System -> Multiple Students -> Which Data Structure is appropriate -> Dictionary

# students = {
#     "101":{
#         "name":"Ravi",
#         "scores":[90,80,90],
#         "skills":{"python","sql","sql"}
#     },
#     "102":{
#         "name":"Mike",
#         "scores":[90,80],
#         "skills":{"python","sql",}
#     }
# }

students = {}

# Build Menu Based System for CRUD 
while True:
    print("=" * 30)
    print("Choose An Option: ")
    print("=" * 30)
    
    print("1 - Create Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - Read Student")
    print("5 - Exit Application")
    
    choice = input("Enter Your Choice (1-5): ")
    
    if choice == "1":
        # Create Student 
        print("=" * 30)
        print("     Adding Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        if student_id in students:
            print("OOPS! Student ID Already Exists!!!!")
        else:
            name = input("Enter Name: ").title()
            scores = []
            while True:
                score_input = input("Enter Score or type done: ")
                if score_input == "done":
                    break 
                if score_input.isdigit():
                    score_input = int(score_input)
                    if 0 <= score_input <= 100:
                        scores.append(score_input)
                    else:
                        print("Invalid Score, Score Should be (0-100)")
                else:
                    print("Invalid Score, Only Digits Allowed")
                    
            skills = set()
            while True:
                skill_input = input("Enter Skill or type done: ")
                if skill_input == "done":
                    break
                else:
                    skills.add(skill_input)
                    
            print(students) # Before Adding
            
            print("========== Student Added ==========")
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            
            print(students) # After Adding
            
    
    elif choice == "2":
        # Updating Student 
        print("=" * 30)
        print("     Updating Student")
        print("=" * 30)
        
    elif choice == "3":
        # Deleting Student 
        print("=" * 30)
        print("     Deleting Student")
        print("=" * 30)
        
    elif choice == "4":
        # Reading Student 
        print("=" * 30)
        print("     Reading Student")
        print("=" * 30)
        
    elif choice == "5":
        # Exit Application 
        print("=" * 30)
        print("     Exiting Application")
        print("=" * 30)
        break
        
    else:
        # Invalid Option
        print("=" * 60)
        print("     Invalid Option Selected, Only Select (1-5)")
        print("=" * 60)