#Variables in python
# 1. 5 Simple variables in Python
# 1. Int
# 2. Float
# 3. Boolean
# 4. String
# 5. None

std_rank_number = 5
std_name = "Vinod"
std_course_fee = 80000.5
std_isactive = True
std_travelling = None

print(type(std_rank_number))
print(type(std_name))
print(type(std_course_fee))
print(type(std_isactive))
print(type(std_travelling))


# Note: Python will infere the data type during the run time. Unlike in Java we have to explicitly mention data type

#2. Type Casting
joining_fee = "9000"
print(int(joining_fee))
print(type(int(joining_fee)))


#3.Concatination and Formatting

first_name = "Vinod"
last_name = " Kumar Reddy"
print(first_name+ ""+ last_name)
print("my first name is " + first_name + " and my last name is" + last_name)
print(f"my first name is {first_name} and my last name is{last_name}")


#4. How to accept Input in Python
# Then input will be always a String so based on the need we need to Type cast
company = input("Enter the User Input")
print(company)
