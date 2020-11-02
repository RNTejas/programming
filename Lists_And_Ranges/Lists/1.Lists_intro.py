print("Lists Introduction")
"""
we can use the '[]' square brackets in three places indexing slicing and in lists 
All iterable are sequence but all sequences are not iterable like Dictionaries

Because lists are iterable we can iterate over them 

"""
# # # # here was the list first
# for item in computer_parts:
#     print(item)
# print()
# print(computer_parts[1])
# print(computer_parts[0:4])
# print(computer_parts[-1])
# computer_parts.append("Mousemat")
# print(computer_parts)

computer_parts = ["CPU",
                  "Monitor",
                  "Keyboard",
                  "UPS",
                  "Mouse",
                  "Mouse-Mat"
                  ]
print(computer_parts)
# computer_parts[3] = "Wireless-Keyboard"
computer_parts[4:] = "TrackBall"   """if you just put the string in the double quotes then you are going to get every 
single letter as the list but if you put the string in the [] as a list then it will fix our problem 
"""
computer_parts[4:] = ["TrackBall"]
print(computer_parts)