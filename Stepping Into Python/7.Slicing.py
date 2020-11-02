print("Slicing is all about Start, Step, End")
"""Python Slicing starts from zero 
    the indexing is "Up to but not Including" like 0:6 then it will print out upto 5 but not including 6
"""
parrot = "Norwegian Blue"
print(parrot[0:6])  #Norveg
# To get the output WE from the string
print(parrot[3:5])
print(parrot[10:14])
""" What else we can do with the slicing
    Let's Find out !!!"""
print(parrot[0:])   # it will print out from 0 till the end
print(parrot[:])    # it will print out the full text
print(parrot[:14])  # it will print out till the end
print(parrot[:9])   # it will print out from 0 till the 8
print(parrot[10:])  # it will print out from 11 till the end

# Negative Slicing
print(parrot[-4:-2])
print(parrot[-4:12])

"""Step in Python"""
print(parrot[0:6:2])
print(parrot[0:6:3])
number = "9,345,844,356,036,458,845"
print(number[1::4])
number = "9,345:844;356 036,458.845"
# print(number[1::4])
separators = number[1::4]
print(separators)
"""Slicing Backwards"""
letters = "abcdefghijlmnopqrstuvwxyz"
backwards = letters[25:0:-1]    #it will print out the letters from z to the letter b because upto but not including
print(backwards)
backwards = letters[25::-1]
print(backwards)
backwards = letters[25:-26:-1]
print(backwards)
#the following line of code print out the 'qpo'
print(backwards[9:12])
#the following line of code print out the 'edcba'
print(backwards[20:])
#the following line of code print out the last eight charecters
print(backwards[0:8])

"""

Python Idioms

if you slice with only negative valur then you will get the last letters how uch you write like if you put -4 then it is going to produce the 
last four letters, if you -24 it is going to produce the last 24 chars

if you put the letter in the 2nd place then it is going to produce the first items in the string print(letter[:1])
"""
print(letters[-4:])      # this will print out the last 4 chars in the letters
print(letters[-26:])     # this will print out the last 4 chars in the letters
print(letters[:4])       # this will print out the first 4 chars
