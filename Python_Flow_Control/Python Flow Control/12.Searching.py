shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None     # doesn't have any value
#for index in range(6) is going to happen here
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break   #break will just humps out of the loop if the condition is True
print("Item found at position {}".format(found_at))

# if item_to_find in shopping_list:
#     found_at = shopping_list.index(item_to_find)
#
# if found_at is not None:
#     print("Item found at position",found_at)
# else:
#     print("{} Not Found".format(item_to_find))
