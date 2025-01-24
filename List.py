"""
List are used to store multiple items in a single variable.
List items are ordered, changeable, allow duplicate values and hold different data types.
List items are indexed which starts with 0.
Lists are denoted with []
"""

# List's are Ordered which means they have defined order and the order will not change
# When a new items is added it will be added at the end of the list

myList = ["apple", "banana", "orange", "grapes", "banana"]
for x in myList:
    print(x)

myList1 = [1, 5, 3, 4, 6, 5]
for x in myList1:
    print(x)

# Key Differences:
# Return value: pop() returns the removed element, whereas remove() does not.
# Argument: pop() takes an index as an argument, while remove() takes the value to be removed.
# Behavior: pop() removes an element at a specific position, while remove() removes the first occurrence of a given value

print(myList1.pop(1))
print(myList1)
# print(myList1.remove(3))

# append() : append the element to the end of the list.
# insert() : inserts the element before the given index.
# extend() : extends the list by appending elements from the iterable.

myList1.append(1000)
print(myList1)

myList1.insert(1,3000)
print(myList1)

myList1.extend(myList)
print(myList1)
