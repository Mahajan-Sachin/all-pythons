# class is a blue print of obj like real world entity which has some properties or behaviour which is rep by class variables & method in programming
# syntx [class class name:]
"""variable
methods"""
#to use variable and method we define object and obj actually creates memory for class
# empty class:
class B:
   age=10
   print(age)
obj=B()#plz comment this line and you will see same result bcoz when we dont make a constructor python make its own and not only a constructor but also a call it now the problem is you can call the obj only 1 time if we dont make our own constructor
obj2=B() #here we can print age only one time


""""""""""""""""""""""""""""""""""""""       """"""""""""""""""""        """"""""""""""""""""        """"""""""""""""""""


class C:
    def __init__(self):#but whenever we make our own construct we have to call it otherwise it will not act also it benefits us by performing it again again and again
       age1=20
       print(age1)
obj=C()
obj2=C()
obj3=C()

