a=int(input("a: "))
def changeglobal():
    a=200
def changelocal():
    a=500
    print("local a value:",a)
print("global  a before function call:",a)
changeglobal