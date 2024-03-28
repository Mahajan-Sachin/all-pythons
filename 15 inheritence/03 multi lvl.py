#in this inheritence we have one parent class and multiple child classes
#syntax: 
"""""class parent
        prop
    class child1(parent)
        prop
    class child2(child1)
        prop
"""
class Father:
    surname="Mahajan"
class Son(Father):
    age=25
    def show(self):
        print("akash",self.surname)
class Gson(Son):
    def Disp(self):
        print("Ankit",self.surname,"who is son of Akash whose father age is",self.age)#here i am trying to make gson inhereit father and son prop
s=Son()
s.show()

Gs=Gson()
Gs.Disp()
Gs.show()

