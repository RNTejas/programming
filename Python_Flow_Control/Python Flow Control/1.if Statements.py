# the input function will returns the value as a string
# name = input("Please enter your name: ")
# age =int(input(f"How old are you, {name}?"))
# print(age)  # this will print out the age but we can't add the string to this number
# print(f"{name}, is {age} Years old")
# age = int(age)
# print(2 + age * 10)
# print(type(age))

a = float(input("Please enter your age in years and month followed by '.' like 12.4, 18.9  : "))
print(a)
#b = range(101, 9999)
#the following code is a voting age generator
if a < 18:
    print( "Come back in {} Years for Vote".format(18 - a))
elif a == range(101, 1000):
    print("You have Died!!!!")
else:
    print("You are enough to Vote")
    print("Please put your Vote in the box")
