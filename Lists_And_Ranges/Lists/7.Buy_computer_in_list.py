available_parts = ["Computer",
                   "Monitor",
                   "Mouse",
                   "Keyboard",
                   "HDMI Cable",
                   "DVD Drive",
                   "MousePad",
                   "Webcam 1080p HD",
                   "MicroPhone with Voice Cancellation"]
current_choice = "-"
computer_parts = []    # creating an empty list
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)] # used the list comprehensions
valid_choices = []
for i in range(1, len(available_parts) + 1):    # + 1 because startswith 0
    valid_choices.append(str(i))

print(valid_choices)
while current_choice != '0':
    if current_choice in valid_choices:

        index = int(current_choice) - 1
        chosen_parts = available_parts[index]
        # removing item if it is already chosen
        if chosen_parts in computer_parts:
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_parts)
        else:
            computer_parts.append(chosen_parts)
            print("Adding {}".format(current_choice))
        print("Your list now contains {}".format(computer_parts))

    else:
        print("Please add options from the list below")
        # for part in available_parts:
            # print("{0} {1}".format(available_parts.index(part) + 1, part)) #instead of using this we can use enumarate
            # the enumerate function is used to return the index of a value

        for number, part in enumerate(available_parts):
            print("{0} {1}".format(number + 1, part))
    current_choice = input()
print(computer_parts)
