"""abstract class is a class that contains one or more abstract methodis called abstract class"""
"""1)Note:An obj of an abstract class cannot be created
2)python provides abc module to work with abstraction
3)we use @abstractmthod decorator to define abstract method
"""
#main point is abstract method is used when we have same action different implementation

"""syntax: from abc import ABC
    class demo(ABC):
        def fun(self):
            #body
        
        @abstractmthod 
        def fun2(self):
            """