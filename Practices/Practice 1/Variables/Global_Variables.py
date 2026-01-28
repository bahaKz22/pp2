x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
