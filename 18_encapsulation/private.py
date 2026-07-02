# Private Access 

class A:
    def __init__(self,a):
        self.__a = a # Private i.e special naming conventions __var 

obj = A(10)

# print(obj.a) # AttributeError: 'A' object has no attribute 'a'

print(obj._A__a) # “You shouldn’t, but you can if you insist”

# Real World Use Case 
class CreditCard:
    def __init__(self,bank,card_number,card_cvv):
        self.bank = bank # Public 
        # self.card_number = card_number # Public Not Recommended 
        self.__card_number = card_number # Private Recommended
        self.__card_cvv = card_cvv