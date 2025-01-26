"""
List are used to store multiple items in a single variable.
List items are ordered, changeable, allow duplicate values and hold different data types.
List items are indexed which starts with 0.
Lists are denoted with []
"""

# List's are Ordered which means they have defined order and the order will not change
# When a new items is added it will be added at the end of the list

# myList = ["apple", "banana", "orange", "grapes", "banana"]
# for x in myList:
#     print(x)
#
# myList1 = [1, 5, 3, 4, 6, 5]
# for x in myList1:
#     print(x)

# Key Differences:
# Return value: pop() returns the removed element, whereas remove() does not.
# Argument: pop() takes an index as an argument, while remove() takes the value to be removed.
# Behavior: pop() removes an element at a specific position, while remove() removes the first occurrence of a given value

# print(myList1.pop(1))
# print(myList1)
# # print(myList1.remove(3))
#
# # append() : append the element to the end of the list.
# # insert() : inserts the element before the given index.
# # extend() : extends the list by appending elements from the iterable.
#
# myList1.append(1000)
# print(myList1)
#
# myList1.insert(1,3000)
# print(myList1)
#
# myList1.extend(myList)
# print(myList1)
#
#
# # Sol1: Using Set to remove duplicates
# newSet = {}
# actualList = ["abc@gmail.com", "def@gmail.com","abc@gmail.com"]
# newSet = set(actualList)
# print(newSet) #{'abc@gmail.com', 'def@gmail.com'}
#
# # Sol2: itreating through List
# newList = []
# actualList = ["abc@gmail.com", "def@gmail.com","abc@gmail.com"]
# for x in actualList:
#     if x not in newList:
#         newList.append(x)
# print(newList)
#



# Question1: Given a list nums, find the sum of all elements in the list.
# inputList = [10, 20, 40]
#
# def sum_of_elements(inp, list_sum):
#     for x in inp:
#         list_sum = x + list_sum
#     return list_sum
#
# print(sum_of_elements(inputList, 0))

# Question2: Write a function to find the maximum element in a list.
inputList1 = [30, 20, 40, 50]

def max_elements(inp):
    print(inp)
    inp.sort()
    len_list = len(inp)
    return inp[len_list -1]
# print(max_elements(inputList1))


max_element = inputList1[0]
def max_elements1(inp, max_element):
    for element in inp:
        if element > max_element:
            max_element = element
    return max_element
print(max_elements1(inputList1, max_element))

# Question3: Remove all duplicates from a list.

nameList = ['Vinod', 'Kumar', 'Vinod', "Reddy"]
uniqueList = set(nameList)
print(uniqueList)

def remove_duplicates(inp_list):
    uniqueList1 = []
    for x in nameList:
        if x not in uniqueList1:
            uniqueList1.append(x)
    return uniqueList1

# print(remove_duplicates(nameList))


# Question: Count the occurrences of an element in a list.

subjectList = ['maths', 'science', 'maths', 'social']

# def count_occurence(list):
#     list1 = list
#     for x in range(len(list1) -1):
#         name = list1[x]
#         print(name)
#         list1.remove(list1[x])
#         print(list1)
#         print(name +str(len(list) - len(list1)))
#
# count_occurence(subjectList)