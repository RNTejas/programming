print("Mutable Objects")
"""
Mutable means it's value can be changed

the mutable objects built-in python are 
    list
    dict 
    bytearray
    set
"""

shopping_list = ["milk",
                 "Pasta",
                 "Eggs",
                 "Bread",
                 "Spam",
                 "Rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["Cookies"]
print(shopping_list)
#the id will not change because the lists are mutable that's the Fact
print(id(shopping_list))
#the items of the another_list are also contains the cookie It shocked me at the Moment😯😯😯🤩🤩😎😎
print(another_list)

# bound the letters and check wheather it is correct
a = b = c = d = e = f = shopping_list
print("adding Mineral water")
c.append("Mineral Water")
print(a)
print(b)
print(c)
print(e)
print(shopping_list)
# The id of these all lists will be same
# there's only one list in the whole process of this page