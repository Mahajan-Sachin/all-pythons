a=input("enter: ")
print(a[1:-1])

b=input("ente: ")
if(len(b)==1):
    print(b)
elif(len(b)==0):
    print("null")
else:
    print(b[-1]+b[1:-1]+b[0])