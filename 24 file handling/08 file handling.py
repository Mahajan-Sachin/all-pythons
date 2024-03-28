try:
    f=open("C:\\Users\\sachi\\OneDrive\\Desktop\\all pythons\\24 file handling\B.txt","r")
    print(f.readlines())
except:
    print("file not available....plz create first!")
else:
    f.close()#rember always close files after using it otherwise it will fuck you
    print("file closed....!")


try:
    f=open("C:\\Users\\sachi\\OneDrive\\Desktop\\all pythons\\24 file handling\A.txt","r")
    print(f.readlines())#now we use a fole which is available
except:
    print("file not available....plz create first!")
else:
    f.close()#rember always close files after using it otherwise it will fuck you
    print("file closed....!")