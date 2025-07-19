import csv # used to read the csv file 
# import pandas as pd # helps work with data easily 
import pandas as pd
import subprocess # gets python run other programs like pandoc 

# STEP 1: Read CSV file
records = [] # empty list called records 
with open("lessons.csv") as csvfile: # opens csv file 
    reader = csv.DictReader(csvfile) # reads each row as a dictionary 
    for row in reader:
        records.append(row) # dicrtionary added to the records list. key is the column name 

# STEP 2: Load into Pandas
df = pd.DataFrame(records) # turns list of dictionaries into tables that panda can easily work with 
# stores it as a variable df 

# STEP 3: Save as Excel for manager
df.to_excel("watch_time_report.xlsx", index=False) # uses the pandas library and exports to an excel file. 
# df is a pandas datafram. an excel spreadhseet in python 
# index=false means not to include row numbers. which would have been included as default. 
# watch_time_reports.xlsx is the name of the output file    

# STEP 4: Save as HTML for boss
df.to_html("watch_time_report.html", index=False) # converts the table into html so it can be veiwed using a browser 

# STEP 5: Calculate total watch time for CEO
# Convert "watch_time" values to numeric (just in case some are strings)
df["watch_time"] = pd.to_numeric(df["watch_time"], errors="coerce") # converts the values in df dataframe into umeric values 
# pd.to_numeric is pandas utility function. converts a series like a column to a numeric function 
# errors="coerce" tells the line to replace any values to Nan if it cant be converted into a number 
total_watch_time = df["watch_time"].sum() # aadds up all the watch time to get the total 

# STEP 6: Create a markdown summary
with open("ceo_report.md", "w") as f: #creates a markdown file 
    f.write("# CEO Video Summary Report\n\n") # writes title 
    f.write(f"**Total Watch Time Available:** **{total_watch_time:.2f} minutes**\n\n") # writes total time watched in bold 
    f.write("_This report is auto-generated._") # writes a string

# STEP 7: Convert markdown to PDF using Pandoc
subprocess.run(["pandoc", "ceo_report.md", "-o", "ceo_report.pdf"]) # runs pandoc immitating how you would type it into terminal 

print("✅ All reports generated successfully.") #final string 
