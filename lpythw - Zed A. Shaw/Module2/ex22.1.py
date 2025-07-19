import sys # imports sys module, allowing you to interact through the command line 
script, input_encoding, error = sys.argv # gets 3 arguments from the command line: script, input_encoding anf error


def main(language_file, encoding, errors): # defines a function named main. takes a file object (language file) and encoding and error handling method
    line = language_file.readline() # reads one line from the lanuage file it is given.

    if line: # if-statement. allows you to test the truth of a variable. 
        print_line(line, encoding, errors) # if there is a line, it sends it to another function print_line. this handles encoding, decoding and printing 
        return main(language_file, encoding, errors) # returns to main line. runs like a loop until there is no more lines left. 


def print_line(line, encoding, errors): # defines a new function, takes the line you want to print, the utf-8 encoding, how to handle errors. 
    next_lang = line.strip() # removes extra spaces from lines. gives new variable next_lang
    raw_bytes = next_lang.encode(encoding, errors=errors) # This line extracts the raw bytes out of next_lng. uses the .encode function. new variable raw_bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors) # this line takes the raw bytes and decodes it back to the original string using the .decode functiion. New variable cooked_string

    print(raw_bytes, "<===>", cooked_string)  # prints this 


languages = open("languages.txt", encoding="utf-8") # opens file named languages.txt in utf-8 encoding and forms new variable as languages. 

main(languages, input_encoding, error) # Calls the main function that was defined earlier above. 