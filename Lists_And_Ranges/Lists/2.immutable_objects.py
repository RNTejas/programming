print("Immutable Objects")
"""
when a object described as IMMUTABLE it means it can't be changed
immutable types built into python are following
    int 
    float                                
    bool(True or False) subclass of int 
    string
    tuple 
    frozenset
    byte
    
immutable mean can't be changed ie
let's take 5 as an int
we can't change the 5 but we can add subtract or do the math with it but we can't change the number 5 
the same for FLOAT
"""

# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
#
# result = False
# print(id(result))

result = "Correct"
print(id(result))
another_result = result
print(id(result))

result += "ness"
print(result)
print(id(result))








