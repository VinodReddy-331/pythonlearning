myDictonary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(myDictonary)
print("Brand name is %s " %myDictonary['brand'])

print(myDictonary['brand'])
print(myDictonary['model'])
print(myDictonary['year'])


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily['child1']['name'])
print(myfamily['child2']['name'])
print(myfamily['child3']['name'])


for x in myfamily.items():
    print(x)