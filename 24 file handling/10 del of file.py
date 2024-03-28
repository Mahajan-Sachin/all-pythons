#file is stored permanently in disk so to del it we import
import os   # operating system
if os.path.exists("C:\\Users\\sachi\\OneDrive\\Desktop\\all pythons\\24 file handling\c.txt"):
    os.remove("C:\\Users\\sachi\\OneDrive\\Desktop\\all pythons\\24 file handling\c.txt")
    print("file del succesfully")
else:
    print("file not available")



 