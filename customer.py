# Customer wants to use mathpackage 

from mathpackage import add 
print(add.msg) 
print("Sum Of Numbers: ", add.add_fun(10,20))

# print(mul.msg) # NameError: name 'mul' is not defined

from mathpackage import add,mul 
print(add.msg) 
print("Sum Of Numbers: ", add.add_fun(10,20))

print(mul.msg)