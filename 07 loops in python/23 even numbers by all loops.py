#while loop
num=int(input("num: "))


sum = 0
i = 0
while(i <= num):
   sum = sum + i
   i = i + 2
print(sum)

#for loop
sum=0
for i in range(num+2):
  if i%2==0:
    sum=sum+i
print("sum =",sum)