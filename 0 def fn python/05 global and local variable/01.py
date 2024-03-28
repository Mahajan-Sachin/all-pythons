a=10
def something():
    a=15
    print(a)#now here we see nothing will be print bcoz a same variable(a) has different variables
    """now a=10 is outside the function sothis is a global variable and a=15 is inside the function so thats why its a local variable
    """""""""""""""
######################################################################################################
"""now understand more"""
b=20
def karan():
    b=25
    print("in fn",b)

karan()#this will print bcoz 25 is inside the fn and a local variable has more priority than a global variable

print("outside",b)