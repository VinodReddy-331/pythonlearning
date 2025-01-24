"""
Python has two primitive loops
1. While Loops
    While loop we can execute a set of statements as long as a condition is true
2. For Loops
    A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
    This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
    With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""

x = 10
#
# while x <= 20:
#     print(x)
#     x = x + 1

# With the break statement we can stop the loop even if the while condition is true:
# while x <= 20:
#     print(x)
#     x = x + 1
#     if x == 15:
#         break


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for name in "vinod":
    print(name)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        print("Fruit is " + fruit + " hence existing the loop")
        break
# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(6):
    print(x)

