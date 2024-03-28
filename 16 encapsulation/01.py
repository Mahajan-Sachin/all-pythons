"""python provides access to all the variable and methods globally
By using encapsulation .we can restrict the variables and methods access globally by making it private or protected"""
#single underscore(protected)
#double underscore(private)
"class and def make a data encaplisation means every class is encapslated but the cindition is var are private or protected"
class A:
    x=5
    _a=10
    __b=20
    print(_a+__b)
    print(_a)
    def show(self):
        print("_a:",self._a)
        print("__b:",self.__b)
obj=A()
obj.show()
print("outside of class :",A._a)
print("outside of class :",A.x)
print("outside of class :",A.__b)#it throws error as it is private
 