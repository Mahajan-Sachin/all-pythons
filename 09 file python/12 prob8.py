content=True
i=1
with open("10 log file.txt") as f:
    while content:
      content=f.readline()
    if "python" in content.lower():
            print(content)
            print("yes python is present")
            print(i)
    i+=1