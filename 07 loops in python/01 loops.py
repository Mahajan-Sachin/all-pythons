i=0
while i<10:
    print("yes"+str(i))
    i=i+1
    
print("done")#never left any space before print otherwise it will consider in loop and answer becomes diff

num = int(input("Enter a number: "))
if num < 0:
    print("Please enter a positive number")
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print("The result is", sum)
