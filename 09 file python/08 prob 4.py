 
with open("sample.text") as f:
    b=f.read()

b=b.replace("karam","#$%$#%#%#")

with open ("sample.text","w") as f:
  f.write(b)
