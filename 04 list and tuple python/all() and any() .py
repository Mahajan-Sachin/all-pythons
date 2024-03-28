#all(): returns true  if all value are true if even one is false it will print false
print(all(1,23,3,45,5,6,7))
print(all(False,"",12,3,4,5,6))

#any():
""" The any() function returns True if any item in an iterable are true, otherwise it returns False.
If the iterable object is empty, the any() function will return False."""
mytuple = (0, 1, False)
x = any(mytuple)
print(x)