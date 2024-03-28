# remember python prioritize last constructor in multiple case
class A:
    def __init__(self):
        name="karan"
        print(name) 

    def __init__(self):
        name="Mohan"
        print(name) 
obj=A()
# 2 types of constructor
"""1)default constructor
2) parameter constructor"""