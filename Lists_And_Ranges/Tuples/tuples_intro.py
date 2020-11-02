# the tuples are like the Read-Only they are not to be changed or modified they're constant

a = "a", "b", "c"
print(a)
"""
    tuples are immutable but it's important because they don't returns the bugs
    
    these are sequence types means you can iterate over them by it's index numbers
    
    tuples data can't be changed but list's data can be changed
"""
# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Night flight", "Budgie", 1981
# imelda = "More Mayhem", "Emelda May", 2011
# metallica = "Ride the lightning", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
#
# table = ("Coffee Table", 200, 100, 75, 34.50)
# area = (table[1] * table[2])
# print(area)
#
# name, length, width, height, price = table
# area = (length * width)
# print(area)

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Night flight", "Budgie", 1981),
          ("More Mayhem", "Emelda May", 2011),
          ("Ride the lightning", "Metallica", 1984), ]

for album in albums:            # name, artist, year use this code instead of album to shorten your code a little bit
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))




























