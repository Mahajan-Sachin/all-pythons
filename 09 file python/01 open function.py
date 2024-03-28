#use of open function to open function
f=open("sample text","r")#here r is used to open it if we dont write no problem by default its r
b=f.read()#here read function is used 
print(b)
f.close()


#we can also read limited chracters
f=open("sample text",)#here r is not used to open it if we dont write no problem by default its r
b=f.read(5)
print(b)
f.close()
