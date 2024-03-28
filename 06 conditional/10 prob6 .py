marks=int(input("enter your marks\n"))

if marks>=90:
    grade="excellent"
elif marks>=80:
    grade="A"
elif marks>=70:
    grade="B"
elif marks>=60:
    grade="c"
elif marks<=50:
    grade="D"
else:
    grade="f"
print("your grade is"+ grade)
