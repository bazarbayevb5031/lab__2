#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#2
for x in range(6):
  print(x)

#3
for x in range(2, 30, 3):
  print(x)

#4
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#5
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#6
for x in [0, 1, 2]:
  pass