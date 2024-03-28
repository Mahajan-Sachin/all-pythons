myDict={
    "fast":"in a quick manner",
    "sachin":"a coder",
   "Marks": [1,3,5,7],
   "anotherdict": {'sachin':'marks'}
}
#dictionary methods
print(list(myDict.keys()))#print the keys of dictionary
print(myDict.values())#print the meaning
print(myDict.items())#print everything in systematic way
print(myDict)#print everything
updateDict={"lovish":"friend",#never forgot to use comma
            "sunny" : "enemy"
             }
myDict.update(updateDict)
print(myDict)
print(myDict.get("sachin"))
print(myDict["sachin"])
print(myDict.get("sachin2"))#returns none as sachin2 not exist
print(myDict["sachin2"])#shows error as sachin 2 is not present