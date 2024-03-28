myDict={
    "fast":"in a quick manner",
    "sachin":"a coder",
   "Marks": [1,3,5,7],
   "anotherdict": {'sachin':'marks'}
}
print(myDict['fast'])
print(myDict['sachin'])
print(myDict["Marks"])
print(myDict["anotherdict"])
print(myDict["anotherdict"]["sachin"])#it means print meaning of sachin in anotherdict
myDict['Marks']=[56,87,98]
print(myDict["Marks"])