def average(a,b):#in this type a and b has  random value
    print("the avg is ",(a+b)/2)
   
average(8,2)


#diff problems
def average(a=9,b=10):#in this type a and b is already has some value
    print("the avg is ",(a+b)/2)
   
average()



#in this we see how default values work
def average(a=9,b=10):
    print("the avg is ",(a+b)/2)
   
average(15)#here by default b=10

#newv approach
def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
      sum=sum+i
    print("avg is:",sum/len(numbers))


average(5,6)
