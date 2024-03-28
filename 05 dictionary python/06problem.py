mydict={
    "Pankha":"fan",
    "dabba":"box",
    "vastu":"item",
    "pradhan":"chief"
}
print("options are",mydict)
a=input("enter the hindi word\n")
print("the meaning of your word is:",mydict.get(a))#this is better as this show no error