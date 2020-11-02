print("String Formatting")
for i in range(1, 13):
    print("{0:2} squared is {1:3} and cubed is {2:4}".format(i, i **2, i**3))
"""
Here the :2, :4 are formatting how many white spaces to leave between the numbers
The above mentioned code is Right Aligned

if you want to align the text to left then you have to put '<' after the colon

if you want to align in the centre then you have to put '^' after the colon
"""
print(())
for i in range(1, 13):
    print("{0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i **2, i**3))

for i in range(1, 13):
    print("{0:2} squared is {1:^3} and cubed is {2:^4}".format(i, i **2, i**3))

print("-"* 50)

print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:<12.50f}".format(22/7))       #'<' is to align the text to the right
print("Pi is approximately {0:<12.70f}".format(22/7))       #'f' after 50,70 is denotes that is a float
print("Pi is approximately {0:<52.50f}".format(22/7))       #:12 is floating point precesion
print("Pi is approximately {0:<62.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))

