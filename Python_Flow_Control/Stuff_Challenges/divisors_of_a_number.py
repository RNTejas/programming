num = int(input("Please enter a number you want to get the divisors of :  "))
for i in range(1, num):
    if num % i == 0:
        print(i)

