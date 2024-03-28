#1) choice. function: returns a random element from a non empty set it will show indexerror if seq is empty
import random
a="bdcbmsbbvsnnszjvzjx.msdjl.d"
print(random.choice(a))

#2)shuffle(list):works for list
import random
l1=[10,29,66,77,"karan","muni"]
l2=[10,29,66,77]
random.shuffle(l2)
print(((l2)))

#radiant(a,b)
print(random.randint(1,5))
print(random.randint(1,5))

#seed() for same random value
for i in range(5):
    random.seed(8)
    print(random.randint(1,100))

#random() generate pseudo-random float fn bw 0 to 1
print(random.random())

#randrange(start,stop,step):random value based on step
print(random.randrange(2,10,2))