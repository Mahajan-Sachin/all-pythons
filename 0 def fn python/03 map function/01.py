list1=[1,2,3,4,5]
def squares(x):
    return x**2
y=print(list(map(squares,list1)))

#-------------------------------------------------------------------------------------------------
"""set1=[10,15,25,30]
def cube(x):
    return x**(1/3)
y=print(list(map(cube,set1)))"""
#--------------------------------------------------------------------------------------------------
x=[1,8,27,64,512]
function2=lambda x:x**(1/3)
print(list(map(function2,x)))
