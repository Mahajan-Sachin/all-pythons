words=["donkey","karan","kimochii"]

with open("sample.text") as f:
    b=f.read()

for word in words:
  b=b.replace(word,"#$%&*&*$^")
  
  with open("sample.text","w") as f:
    b=f.write(b)