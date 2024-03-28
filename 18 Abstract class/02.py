from abc import ABC,abstractmethod 

class Car(ABC):
    def Show(self):
        print("Every car has4 wheels")
    @abstractmethod    
    def Speed(self):#means here speed will be the commonfunction
        pass
class Maruti(Car):
    def Speed(self):
        print("speed is 100km/hr")

class Suzuki(Car):
    def Speed(self):
        print("speed is 70km/hr")

obj=Maruti()
obj.Show()
obj.Speed()

obj2=Suzuki()
obj2.Show()
obj2.Speed()