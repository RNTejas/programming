import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("Please choose an Integer")


highest = 1000
answer = random.randint(1, highest)
print(answer)

guess = 0
print("Please choose a number between 1-{}: ".format(highest))
while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        print("Game Over")
        break

    if guess == answer:
        print("Well done, You guessed it")
        break
    else:
        if guess > answer:
            print("Please chose lower")

        else:
            print("Please chose higher")
