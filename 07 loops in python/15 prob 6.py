n = num=int(input("enter the number: "))
fact = 1
 
for i in range(1, n+1):
    fact = fact * i
 
print("The factorial of given number is : ", end="")
print(fact)