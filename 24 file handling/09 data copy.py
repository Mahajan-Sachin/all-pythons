try:
    with open("C:\\Users\\sachi\\OneDrive\\Desktop\\all pythons\\24 file handling\A.txt") as f2:
       with open("C:\\Users\\sachi\\OneDrive\\Desktop\\all pythons\\24 file handling\c.txt","w") as f3:
           for i in f2:
               f3.write(i)#means every single data in f2 will be written in f3 
except:
    print("file not available....plz create first!")
else:
    f2.close() 
    f3.close()
    print("file closed....!")
