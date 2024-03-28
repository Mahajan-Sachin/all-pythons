"""inheritence which contain only one and one parent class and multiple child classesand each child classes can access parent class property"""
"""
class parent:
    prop
class child1(parent):
    prop
class child2(parent):
    prop"""
class Father:
    surname="kushwaha"
    def Show(self):
        print("My surname is",self.surname)

class Son1(Father):
    def Disp(self):
        print("My name is ankit",self.surname)

class Son2(Father):
    def out(self):
        print("My name is karan",self.surname)

s1=Son1()
s2=Son2()

s1.Disp()  
s1.Show() 
s2.out()


