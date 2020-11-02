import random
answer = random.randint(1, 10)      #random number
print(answer)       # TODO:Remove After Testing
print("Please Guess a number between 1 - 10: ")

guess = int(input())
# if guess != answer:
#     if guess < answer:
#         print("Please choose higher")
#     else:   #guess must be greater than answer
#         print("Please choose lower")
#     guess = int(input())
#     if guess == answer:
#         print("You guessed it second time")
#     else:   #guess must be greater than answer
#         print("Sorry you have not guessed correctly")
# else:
#     print("Well Done you guessed it first time!!")

"""
CHALLENGE Write th ecode like if guess == answer:
"""
if guess == answer:
    print("Well Done, Yo guessed it first time ")
else:
    if guess > answer:
        print("Please choose lower")
    else:
        print("Please choose higher")
        guess = int(input())
    if guess == answer:
        print("Good you gussed it second time ")
    else:
        print("you have not guessed it correctly")