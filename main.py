try:
  a=100
  b=0
  c=a/b
  print("{}/{}={}".format(a,b,c))
except ZeroDivisionError:
  print("Not dividable")
  print("{}/{}=not possible".format(a,b))

def num_in():
  x=int(input("Please give a number:"))
  y=int(input("Please give another number:"))
  try:
    z=x/y
    print(z)
    if(x<0):
      raise TypeError
  except ZeroDivisionError:
    print("Not dividable by zero")
  except ValueError:
    print("Not a number")
  except TypeError:
    print("Data is out of range")

num_in()