def sum(n):
   if n<1:  
    return n#return will behave as break function 
    print("enter a positive number")
   else:
    return sum(n-1)+n
   
print(sum(10))