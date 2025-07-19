import csv # used to read the csv file 
# import pandas as pd # helps work with data easily 
import pandas as pd
import subprocess # hekos python run other programs like pandoc 

# STEP 1: Read CSV file
records = [] # empty list called records 
with open("ex53.csv") as csvfile: # opens csv file 
    reader = csv.DictReader(csvfile) # reads each row as a dictionary 
    for row in reader:
        records.append(row) # dicrtionary added to the records list. key is the column name 

# STEP 2: Load into Pandas
df = pd.DataFrame(records) # turns list of dictionaries into tables that panda can easily work with

# STEP 3: Save as Excel for manager
df.to_excel("watch_time_report.xlsx", index=False) # saves to an excel file. 
# index=false means not to include row numbers

# STEP 4: Save as HTML for boss
df.to_html("watch_time_report.html", index=False) # converts the table into html so it can be veiwed using a browser 

# STEP 5: Calculate total watch time for CEO
# Convert "watch_time" values to numeric (just in case some are strings)
df["watch_time"] = pd.to_numeric(df["watch_time"], errors="coerce")
total_watch_time = df["watch_time"].sum() # adds up all the watch time to get the total 

# STEP 6: Create a markdown summary
with open("ceo_report.md", "w") as f: #creates a markdown file 
    f.write("# CEO Video Summary Report\n\n") # writes title 
    f.write(f"**Total Watch Time Available:** **{total_watch_time:.2f} minutes**\n\n") # writes total time watched in bold 
    f.write("_This report is auto-generated._") # writes a string

# STEP 7: Convert markdown to PDF using Pandoc
subprocess.run(["pandoc", "ceo_report.md", "-o", "ceo_report.pdf"]) # runs pandoc immitating how you would type it into terminal 

print("✅ All reports generated successfully.") #final string 
