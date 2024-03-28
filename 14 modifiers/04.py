"""we can use content of one class in another one"""
class A:
    a=10
    _b=20
    __c=6
    print(a," ",_b," ",__c) 
    def add(self):
        self.__c=self.a+self._b
        print("add: ",self.__c)

class B:#now A and B has no connection 
    def show(self):
        print(A.a) 
        print(A._b) 
       # print(A.__c)#bcoz even when inheritence doesn't work how we can think it will act for just relation
obj=B()
obj.show()