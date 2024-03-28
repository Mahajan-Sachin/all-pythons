class A:
    a=10
    _b=20
    __c=6
    print(a," ",_b," ",__c) 
    def add(self):
        self.__c=self.a+self._b
        print("add: ",self.__c)
class B(A):#child
    def show(self):
        print(self.a)#bcoz a is public it will print
        print(self._b)#bcoz B is inheritance of A so b will print
        print(self.__c)#c is private it will only belongs to A
obj=B()
obj.show()