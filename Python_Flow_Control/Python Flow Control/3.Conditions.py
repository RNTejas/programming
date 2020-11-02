age = int(input("How old are You??"))

# if age >=16 and age <= 65:
# simplifying chined comparison
if 16 <= age <= 65: # BONUS = if you want to use range in the conditions then use this type
    print("have a good day at work")
else:
    print("enjoy your Free time")
print("-"*50)
if age < 16 or age > 65:
    print("Have a good day at work")
else:
    print("Enjoy your free time ")