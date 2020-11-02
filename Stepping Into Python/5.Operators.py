a = 12          #A is not an Expression but 12 do so
b = 3           #B is not an Expression but 3 do so
print(a + b)    #Addition = 15
print(a - b)    #Subtraction = 9
print(a * b)    #36
print(a / b)    #Floating Division = 4.0
print(a // b)   #4 Integer division
print(a % b)    #Reminder = 0

print()
#for i in range(1,a/b):# gives an error because it can't divide integer with floating number
 #   print(i)
for i in range(1,a//b):     # here I is not an expression because it is not considered yet
    print(i)
"""
wherever you use + - * % / // python undestands that it is an Expression but any number used in python also an Expression like12, 34, 1234 etc
there are 25 expressions in this code
but on line 1 and 2 A and B are not Expressions because the are considered to be the expression"""
print()
print()
#Expression precedense
print(a + b /3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a + b)/ 3) - 4) * 12)
print(((a + b)/ 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()
print(a / (b * a) /b)


