#1
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#2
a = 2
b = 330
print("A") if a > b else print("B")

#3
a = 33
b = 200

if b > a:
  pass

#4
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#5
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")