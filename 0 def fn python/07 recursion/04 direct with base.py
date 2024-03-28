#sum of n natural numbers
def sum(n):
    if n==1:
        return 1
    else:
        return (n+sum(n-1))
x=int(input("x: "))
print(sum(x))
#working of above function
'''
step1)when fn called its like sum(4)
step2)4 !=1 so it goes in else (4+sum(3))
step3)in step 2,sum(3) is called it goes in else (3+sum(2))
step4)in step3 sum(2)is called it will(2+sum(1))
step5)in step4 sum(1) called which returns value 1 which make (2+1) which is value for sum(2) and so on
'''