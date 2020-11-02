# to start creating functions you need write def it means define
# after the word def you have to write your function name
# after that don't forget to add () and at last add :
def multiply(x, y):
    product = x * y
    return product


# we are going to use another function called isPalindrome
# you can use multiple functions in one page
def is_palindrome(string):
    return string.casefold().lstrip()[::-1] == string.casefold().lstrip()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    # return string.casefold().lstrip()[::-1] == string.casefold().lstrip()
    # instead of copying and pasting you can just call a function by the following code
    return is_palindrome(string)


word = input("Please enter a word to check Palindrome:")
if palindrome_sentence(word):
    print(f"'{word}' is a Palindrome")
else:
    print(f"'{word}' is not a Palindrome")


print(multiply(10.5, 4))
# to make this program a bit better we need to make this program to take any number the user wants
# you can use the function anywhere in Python
# let's use it in a for loop
# positional arguments mean to store the values in the range or like x, y = 10.5(x) 4(y)
for value in range(1, 11):
    two_times = multiply(2, value)
    print(two_times)

# answer = multiply(10, 10) # this will returns the None because there is nothing to perform
# print(answer)