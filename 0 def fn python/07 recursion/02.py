#now we will do in this way
def anything():
    print("hello")
    anything()#here we call function in function

#now recursion is of two types
"""1)direct  2)indirect"""

#direct example
def demo():
    # properties
    demo()


# indirect be like
def demo():
    # prop
    demo1()

def demo1():
    #prop of demo1()
    demo()#again we call the same fn