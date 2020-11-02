from nested_data import albums

SONGS_LIST_INDEX = 3
SONGS_TITLE_INDEX = 1
while True:
    print("Please choose your album (invalid choice exits:)")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index+1, title))
# # the code on line 10 -13 is working exactly the same as the the code on line 5 - 7

    # for index, value in enumerate(albums):
    #     title, artist, year, songs = value
    #     print(index + 1, title, artist, year, songs)

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break
    print("Please choose your song:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONGS_TITLE_INDEX]
        print("Playing {}".format(title))

    print("=" * 40)
    

