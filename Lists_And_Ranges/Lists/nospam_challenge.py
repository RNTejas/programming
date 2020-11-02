menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage","spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"], 
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]
for meal in menu:
    for index in range(len(meal) - 1, - 1, - 1):
        if meal[index] == 'spam':       # to find the index of meal which contains spam
            del meal[index]             # to delete the 'spam' in the list

    print(",  ".join(meal))             # to join the ', ' and separate them

# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end=", ")
#     print()