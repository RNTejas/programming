name = input("Please enter your name: ")
age = int(input("how old are you , {}?".format(name)))
if 18 <= age < 31:
    print("Hey {} Welcome to the Holiday party".format(name))
else:
    print("Sorry, you can't come to the party")