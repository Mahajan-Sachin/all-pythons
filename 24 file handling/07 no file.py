#now we will try to read data of a file which not even exist
f=open("C:\\Users\\sachi\\OneDrive\\Desktop\\all pythons\\24 file handling\B.txt","r")
print(f.readlines())#now this throws error by saying file not found
"""now we have to handle such files which is the main reason of data handling"""