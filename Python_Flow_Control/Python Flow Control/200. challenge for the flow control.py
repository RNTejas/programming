print("Please choose your choice in the list following")
print("0.\t Quit")
print("1.\t Learn Python")
print("2.\t Go Swimming")
print("3.\t Learn Java")
print("4.\t Have a Dinner")
print("5.\t Go To Bed")

choice = ""
while True:
    #
    if choice == "0":
        break
    elif choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose your choice in the list following")
        print("0.\t Quit")
        print("1.\t Learn Python")
        print("2.\t Go Swimming")
        print("3.\t Learn Java")
        print("4.\t Have a Dinner")
        print("5.\t Go To Bed")

    choice = input()
