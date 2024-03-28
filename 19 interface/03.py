from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def Show(self):
        pass 
    @abstractmethod
    def disp(self):
        pass
class Square(Shape):
    def Show(self):
        pass
class Circle(Square):
    def Show(self):
        print("circle has circular shape")
    def disp(self):
        print("sq has 4 sides")
#now acc to pt 1 we cant make obj of interface which is shape here
 

c=Circle()
c.Show()
c.disp()