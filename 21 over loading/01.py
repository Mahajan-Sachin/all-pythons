"""whenever a class contain more than one method with same name and different types parameter is called oer loading"""
class A:
    def Show(self):
        print("welcome")
    def Show(self,firstname=" "):
        print("welcome",firstname)
    def Show(self,firstname=" ",lastname=" "):
        print("welcome",firstname,lastname)
a=A()
a.Show()
a.Show("ankush")
a.Show("deepak","rohan")
#as we can see we call the same name(just like same person) has different functions(behaviour)