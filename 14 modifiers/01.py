# access modifiers are used to set the limit of memeber accessbility
"""if var=public means accessed everwhere
if _var=protected used in inheritence means used in same classand its inheritence class
if __var=private means only used in main class not even in inheritence"""
class A:
    a=10#public
    _b=20
    __c=6
    print(a," ",_b," ",__c)#here we can see a,b,c are printed easily bcoz they all are in same class
    def add(self):
        print(self._b)
        print(self.__c)
obj=A()
obj.add()
 