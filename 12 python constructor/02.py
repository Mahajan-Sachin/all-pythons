class A:
    def __init__(self):
        age=10
        name="karan"
        print(name,age,)#here we dont have to use self behind name and age bcoz both are defined under def or you can say self
obj=A()

class B:
    age=10
    def __init__(self):
        name="aditya"
        print(name,self.age)#here we  have to use self behind  age bcoz it is  defined under def or you can say self
obj=B()

class C:
    age=15
    def __init__(self):
        name="aditya"
        print(name,age)#this throws error bcoz age was not defined in function
Obj1=C()