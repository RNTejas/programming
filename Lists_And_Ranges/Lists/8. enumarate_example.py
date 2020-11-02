for number, char in enumerate("abcdefghijklmnopqrstuvwxyz"):
    print(number + 1, char)
print("-"*40)

for number, char in enumerate("zyxwvutsrqponmlkjihgfedcba"):
    print(number + 1, char)
print("-"*40)

for t in enumerate("qwertyuiop"):
    index, character = t
    print(t)                 # if you use this code then it will returns the tuple
    print(index, character)  # if you dot want the tuple then use this code

