# when we define a class that inherits all the prop of other class called inheritence
class Father:
    def Lands(self):
        print("having 50 ekar land")
class Son(Father):
    def money(self):
        print("having 1 cr money")
obj=Son()
obj.Lands()#here we can see son obj inhereit lands prop
obj.money()
obj1=Father()
obj1.Lands()
obj1.money()#it shows error 
#types 
"""1)single
2)multiple
3)multi lvl
4)hierchial inheritence
5)hybrid inheritence"""