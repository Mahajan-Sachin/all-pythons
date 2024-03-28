with open("10 log file.txt") as f:
  content=f.read().lower()

if "Python" in content:
  print("yes python is present")
else:
  ("python not present")
