#one parent one child
class A:
    num1=int(input("num1: "))
    num2=int(input("num2: "))
    def add(self):
        print("add",self.num1+self.num2)
    def sub(self):
        print("sub",self.num1-self.num2)
class B(A):
    def mult(self):
        print("mult",self.num1*self.num2)
    def div(self):
        print("div",self.num1/self.num2)
    def rem(self):
        print("add",self.num1%self.num2)
obj=A()
obj.add()
obj.sub()
obj1=B()
obj1.sub()#it will print bcoz of inheritence
obj1.div()
obj.mult()#Attribute error

