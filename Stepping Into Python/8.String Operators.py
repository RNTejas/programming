print("Welcome to the String Operators")
"""
Python3 has 5 Built-in Sequence Types
1.The String type
2.List
3.Tuple
4.Range
5.Bytes and Bytearray

Sequence is an ordered set of items like the above

like "Hello World" in the string there are 11 items and each item s a character and you can iterate over them
"""
string1 = "He's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "New York "

print(string1 + string2 + string3 + string4 + string5)
print("He's " "probably " "pining " "for the " "New York " )

"""You can also multiply the Strings"""
print("Hello " * 5)
# print("Hello " * 5 + 4) #this will gives an error
print("Hello " * (5 + 4))   # this will print out the Hello for the 9 times
print("Hello " * 5 + "4")
"""We can also check if the string is in the string"""
today = "Friday"
print("Fri" in today)   # True
print("day" in today)   # True
print("Sat" in today)   # False
print("New" in "New")   # True
print("Hello" in "World")#False

"""Manipulating Strings"""
"""if you want to add some description before and after the string"""
age = 24
print("My age is " + str(age) + " Years")
print("My age is {0} Years".format(age))
print("There are {0} Days in {1}, {2}, {3}, {4}, {5}, {6}, {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print("There are {0} Days in {1}, {2}, in {3}, {4}, {5}, {6}"
      .format(28,"Feb", 30, "Apr", "Jun", "Sep", "Nov", "Dec"))

print("There are {0} days in Jan {1} days in Feb {0} days in Mar {2} days in Apr {1} days in May {2} days in Jun {0} days in Jul"
      "{0} days in Aug {2} days in Sep {0} days in Oct {2} days in Nov {0} days in Dec".format(31, 28, 30))

print()
print("""
Jan:{0}
Feb:{1}
Mar:{0}
Apr:{2}
May:{0}
Jun:{2}
Jul:{0}
Aug:{0}
Sep:{2}
Oct:{0}
Nov:{2}
Dec:{0}
""".format(31, 28, 30))
