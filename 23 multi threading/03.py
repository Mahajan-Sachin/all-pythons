from time import sleep
class A:
    def run(self):
        for i in range(5):
            print("Akhilesh")
            sleep(1)

class B:
    def run(self):
        for i in range(5):
            print("Ankush")
            sleep(1)

t1=A()
t1.run()

t2=B()
t2.run()
#this will take 10 seconds to print code but now we want it takes 5 sec to print both simultaneously