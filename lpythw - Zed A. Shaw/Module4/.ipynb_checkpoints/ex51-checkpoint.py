import fitz  # imports fitz module from PyMuPDF - lets you open pdf files and read them 
import sys # lets open command-line args 

# Get the PDF file path from command-line arguments
pdf_path = sys.argv[1] # argv[1] in commmand line should be pdf file name. this picks it up
# stores it as pdf_path variable

# Open the PDF file
doc = fitz.open(pdf_path) # fitz opens the pdf file so python can read it. stores all the pages as doc 

# Extract text from all pages
full_text = "" # creates an empty string 
for page in doc: # goes through each page in doc 
    full_text += page.get_text() # gets textusing page.get_text()
    # then appends it to the empty string "full_text"

doc.close() # closes doc 

# Split the text into lines
lines = full_text.split("\n") # breaks all the texts into lines using the esca[pe sequence /t
# creates a list/variable called lines

# Find and print the line starting with "Reporting Period"
for line in lines: # goes through each line 1 by 1 
    if line.strip().startswith("Reporting Period"):  #  checks if lin starts with "Reporting Period"
        print("✅ Found:", line.strip())
        break  # Stop after first match

# in     if line.strip().startswith("Reporting Period")
# .strip() - removes any extra white space from the start and the end of the line 
# .startswith("Reporting Period") - checks if the start of the line has the words we are looking for in it in the cleaned up lines. 

# steps
# 1. import fitz and sys modules 
# 2. set arg variable for pdf file from the command line 
# 3. open file and save as a variable 
# 4. close doc
# 5. split lines and use \n escape sequence
# 6. strip lines of extra space at beginning and end 
# 7. if line found print a message along with the line 
# 8. break LookupError




