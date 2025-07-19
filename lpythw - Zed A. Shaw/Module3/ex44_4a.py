def new_player(name, age, position): # defining a function with 3 arguments 
    player = { # created a dictionary
        "name": name, 
        "age": age, 
        "position": position, 
    }

    def hit(words):
        print(f"{player['name']} has {words}")

    player['hit'] = hit

    return player

nirmal = new_player("Nirmal", 29, "Winger")

position = "winger"

tyty = {
    "position": position,
}

nirmal['hit'](f"struck his opponent")

