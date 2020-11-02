data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]
# Test, Test and Test again and then Test Again
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]
# data = [1000, 10002, 22232]
# data = []


# # to remove the objects from the list using slice
# del data[0:2]
# print(data)
# del data[14:]
# print(data)
min_valid = 100
max_valid = 200
##
## for index, value in enumerate(data):
##     if (min_valid > value) or (max_valid < value):
##         del data[index]
##
## print(data)

# safely removing items from a list

# process the low values in the list
stop = 0        # because we want to check the list till the end
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop)     # for debugging
del data[:stop]
print(data)


# process the high values in the list
start = 0       # because we want to check the list from the end
for index in range(len(data) - 1, - 1, - 1):     # -1 = start value, -1 = stop value, -1 = step value
    if data[index] <= max_valid:
        start = index + 1    # we are adding 1 because of we are deleting the item from last but including the last one
        break
print(start)        # for debugging
del data[start:]    # + 1:]
print(data)





