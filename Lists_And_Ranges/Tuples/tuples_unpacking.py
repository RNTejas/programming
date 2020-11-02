a = b = c = d = e = f = 42      # chained comparison
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("Tuple Unpacking")

data = 1, 2, 76        # data is representing the Tuple
x, y, z = data         # data unpacking
print(x)
print(y)
print(z)

print("List Unpacking")
"""
Unpacking a list can cause some problems because because lists are mutable and that doesn't happens with the tuples 
because they're immutable
"""
data_list = [12, 13, 15]
p, q, r = data_list
print(p)
print(q)
print(r)
