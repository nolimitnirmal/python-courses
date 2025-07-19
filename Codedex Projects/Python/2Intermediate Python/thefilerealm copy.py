
liked_songs = {
    "Drake" : "somebody loves me",
    "Lil Baby" : "Freestyle",
    "yeat" : "Call me"
}


def write_dict_to_file(songs, file_name):
    with open(file_name, "w") as file:
        file.write("Liked Songs : \n")
        for song, artist in songs.items():
            file.write(f"{song} by {artist}\n")
    print("successfully added liked songs to file")


write_dict_to_file(liked_songs, "fave_songs.txt")

