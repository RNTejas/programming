flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lilly",
]
# for flower in flowers:
#     print(flower)

separator = "  |  "     # we can use anything we want like the ', '
output = separator.join(flowers)
print(output)

# the easiest way of doing the 13  - 17 line of code is
print(", ".join(flowers))
"""
NOTE: you must have all the strings in the list if you use integers or so then the program will crash
"""