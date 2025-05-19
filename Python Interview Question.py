# 1. What is the output from the below String?
str = "India"

print(str[-1])  # -1 will access the last index of the string #Ouput is a
print(str[-2])  # output "i"

print(str[:-1])  # str[start:end] is used for slicing a string.#Output Indi
print(str[:-3])  # ouput "In"

print(str[::-1])  # str[start:end:step] is the complete syntax for string slicing.
#: without numbers before and after it means "from the beginning to the end".


# Take below Input and print the given expected Output?
list1 = ["my", "name"]
list2 = ["is", "John"]
list1.extend(list2)
print(list1)
# or
list4 = list1 + list2
print(list4)


def required_str(inp_list, str):
    for x in list1:
        str = str + x + " "
    return str


print(required_str(list1, ""))

# 3. Convert the List into a Dictonary ?
inputList1 = ["name", "id"]
inputList2 = ["Vinod", 1]
outpuDict = {}
for x in range(len(inputList2)):
    outpuDict[inputList1[x]] = inputList2[x]

print(outpuDict)

# 4. Find the duplicate characters in a given List
inpList = ['India', 'Is', 'My', 'Country']
finalStr = ""
uniqueCharacterSet = set()
duplicateCharacterList = []
duplicateCharacterDict = {}
for x in inpList:
    finalStr = finalStr + x.lower()
print(finalStr)

# india
def duplicate_CharList(str):
    for x in str:
        if x in uniqueCharacterSet:
            duplicateCharacterList.append(x)
        else:
            uniqueCharacterSet.add(x)
    return duplicateCharacterList

print("Print Duplicate List")
# print(duplicate_CharList(finalStr))


# india
# 5.Count the duplicate characters in a given List values
def duplicate_CharCount(str):
    for x in str:
        counter = 1
        if x in uniqueCharacterSet:
            counter = counter + 1
            duplicateCharacterDict[x] = counter
        else:
            uniqueCharacterSet.add(x)
            duplicateCharacterDict[x] = counter #{"i":1, "n": 1, "d": 1}
    return duplicateCharacterDict

print("Print Duplicate Char Count")
print(duplicate_CharCount(finalStr))

# dict = {"name": "vinod"}
# dict['id'] = 10
# print(dict)
