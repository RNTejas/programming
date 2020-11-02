pangram = """The quick brown
fox jumps\tover 
the lazy dog"""

words = pangram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
# first way to solve the challenge str to int
values_list = numbers.split()
# for index in range(len(values_list)):
#     values_list[index] = int(values_list[index])
# print(values_list)

# second way to convert str to int
integer_values = []
for values in values_list:
    integer_values.append(int(values))