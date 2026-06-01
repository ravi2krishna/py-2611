# Indentation

print("Hello")
# print("Python") # IndentationError: unexpected indent

# In Python, if statement is used to execute a block of code 
# only when a specific condition evaluates to True

# -> Indentation refers to Code Structuring and code blocks 

# if True:
# print("This") # IndentationError: expected an indented block after 'if' statement 
# print("is")
# print("the")
# print("block")
# print("of")
# print("code")
# print("to")
# print("execute")
 
print("This") # line 21 to 28 is not block of code
print("is")
print("the")
print("block")
print("of")
print("code")
print("to")
print("execute") 

print("==============")
    
if True:
 print("This")
 print("is")
 print("the")
 print("block")
 print("of")
 print("code")
 print("to")
 print("execute")
 

# Inconsistent number of spaces leads to Errors i.e IndentationError
# if True:
#  print("This")
#   print("is")
#    print("the")
#  print("block")
#  print("of")
#  print("code")

print("==============")

# Consistent number of spaces 
if True:
  print("This")
  print("is")
  print("the")
  print("block")

print("==============")

if True:
            print("This")
            print("is")
            print("the")
            print("block")

print("==============")
            
# Recommended way is to use 4 spaces i.e single Tab
if True:
    print("This")
    print("is")
    print("the")
    print("block")
    print("of")
    print("code")
    print("to")
    print("execute")