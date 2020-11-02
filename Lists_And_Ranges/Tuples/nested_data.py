albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]
# uncomment the code to run the code in this window otherwise thee program will crash on the jukebox_menu.py
# for name, artist, year, songs in albums:
#     print(f"Album: {name}, Artist: {artist}, Year: {year}, Songs: {songs}")
# print()
#
# # printing individual values in values from a tuple containing tuple of list
#
# album = albums[3]
# print(album)
#
# songs = album[3]
# print(songs)
#
# song = songs[2]
# print(song)
# print(song[1])
#
#
# mayhem = albums[1][3][2][1]
# # the above line of code goes in to the album and searches for the index 3 inside index 3 searches another index 3
# # inside that it finds 2 and at last inside 2 it finds 1 and get stored
# print(mayhem)