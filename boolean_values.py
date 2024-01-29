#1
print(10 > 9)
print(10 == 9)
print(10 < 9)

#2
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#3
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#4
x = 200
print(isinstance(x, int))

#5
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")