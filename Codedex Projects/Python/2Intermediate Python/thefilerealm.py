

# Define a dictionary to store liked songs with their artists
liked_songs = {
    "Bad Habits": "Ed Sheeran",
    "I'm Just Ken": "Ryan Gosling",
    "Mastermind": "Taylor Swift",
    "Uptown Funk": "Mark Ronson ft. Bruno Mars",
    "Ghost": "Justin Bieber"
}

# Function to display and write liked songs to a file

def write_liked_songs_to_file(songs, file_name): # defines a new funtion that takes 2 arguments. one for songs and one for the file you will create 
    with open(file_name, 'w') as file: # with closes the file that you open automatically. in write mode and saves it as variable "file"
        file.write("Liked Songs:\n") # writes the first line of the text file. this is the title.
        for song, artist in songs.items(): # loops through the dictionary that we pass into the funstion as an argument "song". uses items so that it will loop in pairs. 
            file.write(f"{song} by {artist}\n") # writes a string for each loop. 
    print(f"Successfully added Liked songs to {file_name} ❤️") # prints a final message. 

# Write liked songs to a .txt file
write_liked_songs_to_file(liked_songs, "liked_songs.txt") #