with open("another text 02","r") as f:
    a=f.read()
with open("another text 02","w") as f:
    a=f.write("me")#check another text 02 "me" is written in it
print(a)