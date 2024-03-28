def team(name, project, members=None):
    team.name= name
    team.project= project
    team.members= members
    print(name, "is working on an", project)
 
team("FemCode", project = "Edpresso")



def fact(n):  
    if (n==1 or n==0):
     print("invalid bsdk")
    else:
       n * fact(n - 1);  
  
num = int(input("n: "))  
fact(num)
print("Factorial of",num,"is",)  
fact(num)