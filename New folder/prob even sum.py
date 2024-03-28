''''num = int(input("enter the number: "))
sum=0
i=0
while(i<=num):
       sum = sum+i
       i=i+2
       print(sum)
print(sum)  

"""odd"""
num = int(input("enter the number: "))
sum=1
i=0
while(i<=num):
       sum = sum+i
       i=i+2
       print(sum)
print(sum)  


i=1
while i<6:
       print(i)
       i+=1
else:
       print("i is no longer less than 6")'''

num=int(input("num: "))
i=0
sum=0
if(num>=0):
       while(i<=num):
              sum=sum+1
              i=i+1
else:
       while i>num:
              sum=sum+1
              i=i-1
print("sum:",sum)



fruits=["apple","mango","strawbery","papaya"]
for x in fruits:
       print(x)
for x in "mango":
       print(x)


mydict={"karan":"string",
        1:int,
        "honey":"a coder"}
print(mydict)
for x in mydict:
       print(x)
for x in "karan":
       print(x)