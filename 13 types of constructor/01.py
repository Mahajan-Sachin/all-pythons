#default constructor are also called empty constructor bcoz it doesnt have any any parameters
# if we dont define any constructor python consider ita default
class A:
    name="Akhilesh"
    def __init__(self):#default
        print(self.name)
obj=A()


class B:
    name="harsh"
    age=22
    def __init__(self):#default
        print(self.name)
    def show(self):
        print(self.age)
obj=B()#now you can observe that even age has self it is in last still it didnt work bcoz it doesnt have any constructor



class C:
    name="Deepak"
    age=25
    def __init__(self):#default
        print(self.name)
    def show(self):
        print(self.age)
obj.show()#this is saying obj of show to work