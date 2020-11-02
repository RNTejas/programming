pangram = "the quick brown fox jumps over the lazy dog"

letter = sorted(pangram)
print(letter)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.8]
sorted_num = sorted(numbers)
print(sorted_num)
print(numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)  # use this to make case insentive sorting
print(missing_letter)

# Another example for case insentive sorting
names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "micheal"
         ]
names.sort(key=str.casefold)
print(names)
sorted_names = sorted(names, key=str.casefold)
print(sorted_names)