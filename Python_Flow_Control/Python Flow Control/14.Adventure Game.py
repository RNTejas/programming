available_exits = ["north", "south", "east", "west"]
chosen_exit = ''
while chosen_exit.casefold() not in available_exits:
    chosen_exit = input("Please enter the direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break
print("aren't you Glad that you are out from there")

