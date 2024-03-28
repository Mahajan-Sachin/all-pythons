a={}#this is not a empty set set this is a actually empty dictionary
print(type(a))

''' a empty set can be formed in below way'''
b=set()#'''this is a empty set'''
print(type(b))


#adding values
b.add(1)
b.add(7)#in line9 and 10 7 is added 2 times but it will print only 1 time bcoz  again repetion not allowed
b.add(7)
b.add(9)
print(b)
b.add((3,6.8,8,0,5))#tupple can be added
print(b)

#some functions
print(len(b))
b.remove(7)
print(b)
print(b.pop())#remove random value from set
print(b)
b.sort()#set cant be sort out


#which cant be added
b.add([3,6.8,9])#this show error bcoz list cant be added in set
b.add({4:5})#again dictionary also cant be add
print(b)