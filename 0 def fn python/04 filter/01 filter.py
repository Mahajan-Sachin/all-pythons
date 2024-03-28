#works like map function
def even(e):
    return e%2==0
nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(even,nums))
print(evens)

a=lambda x:x%2==0
n=[1,2,3,4,5,6,7,8,9]
eve=list(filter(a,n))