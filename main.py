#try - exceptions (ZeroDivisionError, NameError, ValueError, TypeError)
"""
try:
  a=100
  b=0
  c=a/b
  print("{}/{}={}".format(a,b,c))
except ZeroDivisionError:  #----------
  print("Not dividable")
  print("{}/{}=not possible".format(a,b))

def num_in():
  x=int(input("Please give a number:"))
  y=int(input("Please give another number:"))
  try:
    z=x/y
    print(z)
    if(x<0):
      raise TypeError  #----------
  except ZeroDivisionError:  #----------
    print("Not dividable by zero")
  except ValueError:  #----------
    print("Not a number")
  except TypeError:  #----------
    print("Data is out of range")

num_in()
"""
def ve1():
  try:
    val=int("abc")
    print(i)
  except ValueError as v:
    print(f"Caught a ValueError at {v}")

ve1()

def ve2():
  try:
    val=float("abc")
    print(i)
  except ValueError as v:
    print(f"Caught a ValueError at {v}")
  else:
    print("No exception occured")

ve2()


def typeErrorCase():
  