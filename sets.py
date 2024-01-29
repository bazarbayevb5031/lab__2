#1
thisset = {"apple", "banana", "cherry"}
print(thisset)

#2
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
#or
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#3
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#4
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#5
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#6
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#or
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#7
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#8
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#9
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#10
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#11
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)