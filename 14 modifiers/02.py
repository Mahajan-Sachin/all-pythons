class A:
    a=10
    _b=20
    __c=6
    print(a," ",_b," ",__c)#here we can see a,b,c are printed easily bcoz they all are in same class
    def add(self):
        self.__c=self.a+self._b
        print("add: ",self.__c)
obj=A()
obj.add()
print(obj.a)
print(obj._b)
print(obj.__c)#now it will throe error