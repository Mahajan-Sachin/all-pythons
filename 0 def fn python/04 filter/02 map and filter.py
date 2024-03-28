a=lambda x:x%2==0
n=[1,2,3,4,5,6,7,8,9]
eve=list(filter(a,n))

b=lambda y:y*2
print(list(map(b,eve)))