def Person_new(name, age, eyes): # defining a function with 3 arguments 
    person = { # created a dictionary
        "name": name, 
        "age": age, 
        "eyes": eyes, 
    }

    

    def talk(words): # definining a new function inside the first one
        print(f"I am {person['name']} and {words}") #Format string 

    person['talk'] = talk  #takes the output of the format string from the function above and stores it as a new value in the person dictionary as 'talk'

    return person # returns the dictionary with the 'talk' key to where the function was called. 

becky = Person_new("Becky", 39, "green") # calling for person_new function created and stored as a variable

becky['talk']("I am talking here!") 

# Person_new("Becky", 39, "green")['talk']("I am talking here!")

# Person_new("Becky", 39, "green") >>>> this part is gonna call the function person_new, and bring up the dictionary 

# once the dictionary is pulled up it will run this function >>>> ['talk']("I am talking here!") which is talk("words") 