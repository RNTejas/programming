print("Welcome to the Simple Calculator")
print("a.Addition")
print("b.Subtraction")
print("c.Multiplication")
print("d.Division")

user_choice = input("Please choose your Operator:")
if user_choice == "a":
    input1 = float(input("Please enter your first number:"))
    input2 = float(input("Please enter your second number:"))
    print(input1 + input2)
elif user_choice == "b":
    input1 = float(input("Please enter your first number:"))
    input2 = float(input("Please enter your second number:"))
    print(input1 - input2)
elif user_choice == "c":
    input1 = float(input("Please enter your first number:"))
    input2 = float(input("Please enter your second number:"))
    print(input1 * input2)
elif user_choice == "d":
    input1 = float(input("Please enter your first number:"))
    input2 = float(input("Please enter your second number:"))
    print(input1 / input2)
else:
    print("Please choose a valid Operator")
