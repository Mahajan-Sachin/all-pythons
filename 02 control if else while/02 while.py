#loop statement
# 1)while it will act until situation becomes false
#every loop has 3 parts
"""
1) initialization
2) Condition till where the functions ends
3) increment/decrement/or whatever 
if anyone is misssing then it will fail
"""       


"""  
For loop is usedto iliterate/retrive over a seq (such as list.tuple or string).
use it when you know how many times you want to execute it
example
colors=["blue,"green,"yellow,"orange]
for i in colors:
print(i)

a while is used to repeat execute a code as long as a certain condition is true.
use when you dont know how many times you want to execute
"""

colors=["red","orange","grren","yellow"]
for i in colors:
    print(i,)

i=1
while i<5:
     print(i)
     i+=i

i=15
while i<5:
     print(i)
     i+=i
else:
     print(i)

# while not goes for false or you can say else like: simple words statement directly under not is for true 
x=0
while not (1<=x<=100):
     x=int(input("enter a sexy no: "))
print("valid no")
    

for i in range(3):
     x=int(input("plz enter a no bw 1 and 100: "))
     if 1<=x<=100:
          print("valid no: ",x)
          break
     else:
        print("invalid number.try again")


