
liked_songs = {
    'drake' : 'sombody loves me',
    'lil baby' : 'all in', 
    "gunna" : 'one one tonight'
    }


def write_liked_songs_to_file(songs, file_name):
    
    with open(file_name, 'w') as file:
        file.write("Liked songs: \n")
        for artist, song in songs.items():
            file.write(f"{song} by {artist} \n")
    print("all done")

write_liked_songs_to_file(liked_songs, "fave_songs.txt")


