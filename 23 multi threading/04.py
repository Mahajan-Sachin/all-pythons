from time import sleep
from threading import Thread
class A(Thread):
    def run(self):
        for i in range(5):
            print("Akhilesh")
            sleep(1)
     

class B(Thread):
    def run(self):
        for i in range(5):
            print("Ankush")
            sleep(1)

t1=A()
t1.start()#we use start to start fn

t2=B()
t2.start()
#now the problem is if we want to do some other task it will interfare with it to confirm it you can see below print statement by uncomment it
#print("karan")