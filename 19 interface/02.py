from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def Show(self):
        pass#here we cant write the code bcoz technically we dont know about shape
class Square(Shape):
    def Show(self):
        print("square has 4 side...")

class Circle(Shape):
    def Show(self):
        print("circle has circular shape")

#now acc to pt 1 we cant make obj of interface which is shape here
s=Square()
s.Show()

c=Circle()
c.Show()