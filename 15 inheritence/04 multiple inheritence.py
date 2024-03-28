"""inheritence which contain more parent clases and only one child class is called multiple inheritence"""
"""
syntax:
class parent1
    prop
class parent2
    prop
class parent3
    prop
     -------- - - - -  
class child(parent1,parent2----)"""
class Akhilesh:
    Back="oracle Db and java"
    def Backend(self):
        print("Backend task implemented using:",self.Back)
class Ankush:
    Front="Html and css"
    def Frontend(self):
        print("Frontend task implemented using:",self.Front)
class Teamlead(Akhilesh,Ankush):
    def show(self):
        print("dynamic website created.....")
T=Teamlead()
T.Backend()
T.Frontend()
T.show()
