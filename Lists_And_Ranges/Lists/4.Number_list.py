# even = [2,4,6,8]
# odd = [1,3,5,7,9]
#
# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
# print()
# print(len(even))
# print(len(odd))
#
# """
# Now, let's introduce to you the new feature of python that is COUNT
# Let's get started
# """
# print("Let's Use Count")
# print("mississippi".count("s"))
# print("mississippi".count("is"))
# print("mississippi".count("iss"))

"""
Now we will introduce to the another new function called EXTEND
by using this we can add the two iterables but not ijn the sorted form so
Let's have a look!! 
"""
# print("Let's use EXTEND")
# even.extend(odd)
# print(even)

# another_even = even
# print(even)
# print()
"""
As I have told you that we can add together but not in the sorted form
To do that we have to use another function called the 'sort'
Let's have a look!! 

"""
# even.extend(odd)
# print(even)
# even.sort()
# print(even)

empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)
