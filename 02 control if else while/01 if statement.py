#control statement is of two types 1)conditional/selection   2)looping
"""now we will discuss abt conditional"""
#if else....
a=int(input("a: "))
if a%2==0:
    print("even")
else:
    print("odd")


age=int(input("enter your age: "))
if age>18:
    print("valid")
else:
    print("why in hurry")
print("speed thrills but kill")#this print doesnt depend on conditions


#only if
age=int(input("enter your age: "))
if age>18:
    print("valid")
print("speed thrills but kill")#this print doesnt depend on conditions

#if else if .... 
handsome="true"
good_salary="false"
if handsome=="true" and good_salary=="true":
    print("you will marry heroine")
elif handsome != "true" and good_salary=="true":
    print("you marry a sundar kanya")
elif handsome=="true" and good_salary!="true":
    print("you marry a girl")
else:
    print("gand mra")
#nested if else
age =17
own_car='false'
if age>=18:
    if (own_car =="true"):
        print("drive your car")
    else:
        print("purchase it now")
else:
    print("bsdk 18+ ka bad")
