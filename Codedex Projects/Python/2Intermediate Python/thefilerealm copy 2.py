liked_songs = {

    "drake" : "somebody loves me", 
    "lil-baby" : "Freestyle",
    "gunna" : "south to west"
}


def write2file(songs, file_name):
    with open(file_name, "w") as file:
        file.write("Liked Songs : \n")
        for song, artist in songs.items():
            file.write(f"{song} by {artist}\n")
    print("All done")


write2file(liked_songs, "fave_songs.txt")





    