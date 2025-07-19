  
print("I am 6'2\" tall")
print('I am 6\'2" tall.')

# the escape sequence '\' is used to enter difficult-to-type characters into a string
# using | tells python that the ' or " inside the string isnt a real double quote or single quote

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat "

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies 
\t* Catnip\n\t* Grass 

"""
# \n puts the text after into a new line 
# \t - means horizontal tab (indenting)

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

