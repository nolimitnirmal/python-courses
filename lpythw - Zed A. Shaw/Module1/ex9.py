
days = "Mon Tue Weds Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# you are using an "escape sequence"
# it is a way for you to add formatting, vertical space, tabs, special characters etc..
# the letter used after the escape sequence determines what it does. 
# in this case, it is "n"
# meaning a "new line"
# if you want to add a special character, you can use a processing backslash \ and them add it


# if you want the months in a new line. (From Jan)
# start like this "\nJan/nFeb\..."

print("Here are the days: ", days)
print("Here are the months: ", months)

# when you use 3 double quotes, you can write as many strings as you want 
# you can add quotes and double quotes. 

print("""
There's something going on here.
With the three double quotes.
We'll be able to type as much as we like. 
Even 4 lines if we want, or 5, or 6.
""") # when python runs into the 3 quotes again it knows to stop

# Slam the text all the way to the left. pythom uses indentations for a lot. 
# the spaces will stay with indentations unless you get rid of it


