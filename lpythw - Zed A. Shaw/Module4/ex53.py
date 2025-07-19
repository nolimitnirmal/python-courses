import json # imports json module 
import csv # imports csv module, allows you to read csv 
from collections import defaultdict 

# Step 1: Load local cached JSON data
with open("course.json") as f: # opens a file named course.json in read mode by default and assigns it to variable f
# remember with always closes the file when done 
    course_data = json.load(f) # parses json file and converts to python object then saves it as course_data 

with open("media.json") as f: # opens media json in read only and saves it as f
    media_data = json.load(f) # parses file and saves it as variable media_data

# Step 2: Map lesson_id to total video length
lesson_watch_times = defaultdict(float) # defaultdict is a function from the collection moduel. its a dictionary assigns a default value for any new key
for media in media_data: # starts a loop each time a media is inside media data 
# media_data is the parsed JSON/dic fro media.json
    if media["media_type"] == "video": # for each media tem check if the media_type is a video 
        lesson_watch_times[media["lesson_id"]] += media["length"] # for the medias, get the lesson_id and add this video length to total watch time (lesson_watch_times)

# Step 3: Prepare CSV data for lessons. These are the rows for the CSV output
lesson_rows = [] # creates an emtpy list
module_rows = [] # creates an emtpy list
total_watch_time = 0.0 # single summary row for whole course. initialises total watch time 

for module in course_data["modules"]: # loopes through every module in course data 
    module_total = 0.0 # starts tracking total viedo watch time 
    for lesson in module["lessons"]: # loops through each lesson in that module  
        lesson_time = lesson_watch_times.get(lesson["id"], 0.0) # gets total watch time for this lesson from the lesson watch time dict, if lesson watch time isnt found use 0, 0 as dict  
        total_watch_time += lesson_time # adds lesson time to overall course total 
        module_total += lesson_time # adds lesson time to modules total 
        lesson_rows.append({ # builds lesson rows with 4 titles shown below
            "module_title": module["title"],
            "lesson_title": lesson["title"],
            "lesson_id": lesson["id"],
            "watch_time": lesson_time
        })
    module_rows.append({ # builds module rows with 3 titles shown below 
        "module_title": module["title"],
        "watch_time": module_total
    })

course_row = { # creates one row for entire course 
    "course_title": course_data["title"],
    "watch_time": total_watch_time
}

# Step 4: Save CSV reports
# this part writes each list of rows to a seperate CSV file.
with open("lessons.csv", "w", newline="") as f: # opens a file safely in wrtie mode "w". remember that using "with" closes the file that you opene automatically
    writer = csv.DictWriter(f, fieldnames=lesson_rows[0].keys()) # 
    writer.writeheader() #
    writer.writerows(lesson_rows)

with open("modules.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=module_rows[0].keys())
    writer.writehzeader()
    writer.writerows(module_rows)

with open("course.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=course_row.keys())
    writer.writeheader()
    writer.writerow(course_row)

print("✅ CSV reports generated: lessons.csv, modules.csv, course.csv")
