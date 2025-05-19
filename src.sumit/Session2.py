# 1. Arthematic Operators
# +, - , /, %, *   Precedence is from Left to Right (* and / will have higher priority)
# 10 + 3 + 5  (i) 10 +3 = 13 ; (ii) 13 + 5 = 18
import math

tg_ap_distance = 680
tg_ka_distance = 590.5
additional_distance = 2
total_distance =  tg_ap_distance * additional_distance + tg_ka_distance * additional_distance
print(total_distance)
print(tg_ap_distance/2)
print(tg_ap_distance%2)
print(tg_ap_distance ** additional_distance)

print(math.ceil(tg_ka_distance))
print(math.floor(tg_ka_distance))


# Conditional

marks = int(input("Enter the student marks : "))

if marks >= 35:
    if marks >=80:
        print("Grade A")
    elif marks >=60 and marks <80:
        print("Grade B")
    else:
        print("Grade C")
else:
    print("Din't secured pass marks to qualify. Please do re-attempt March")


#Assingment: Take two inputs( age >18 and crime records and no crime then eligible for vote)
age = int(input("Enter the age: "))
crimerecords = bool(input("do have any crime record? "))

print('--------------')
print(17>=18)
print( False & True )
print('--------------')
if (age >=18 & crimerecords == False):
    print("Eligible For Voting")
elif (age <=18 & crimerecords == False):
    print("Age is less than 18 not Eligible For Voting")
elif (age >=18 & crimerecords == True):
    print("Age is greater than 18 but have crime records So Not Eligible For Voting")
else:
    print("Age is less than 18 and also have crime records So Not Eligible For Voting")