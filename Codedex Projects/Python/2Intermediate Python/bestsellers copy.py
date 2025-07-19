import csv 

max_sales = 0 
best_selling_book = None

# TASK 1

with open("Bestseller - Sheet1.csv", "r", encoding= "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_file.readline() # this is a built in method in python to read a line. used here to skip the header

    for row in csv_reader: # starts a for loop for each for in the csv file 
        current_sales = float(row[4]) # for each row it stores the sales in millions column value as a variable "current_sales" and converts it into a float 

        if current_sales > max_sales: # starts another if loop if the current sales is > max_sales. the first row the max sales is automatically going to be > 0. which is the initial value. then as it goes through each row, if it is no above the max value the loop will not be initiated. 
            
            current_sales = max_sales # whatever the max value is, it will be stored as the current sale. 
            best_selling_book = row # at the end of the for loop, whatever row has the max_sales is stored as the best_selling_book. 

# TASK 2 - Storing the information from task 1 into a new file 

output_file_path = "best_seller_info.csv" # file name is stored as a variable 

with open(output_file_path, "w", newline="") as output_file: # with loop to open the file in writer mode and saved as output_file 
    csv_writer = csv.writer(output_file) # user csv.writer funtion to write into the output_file. this is stored as a variable. csv_writer is now an object to the csv module and can use csv methods on it. 

    csv_writer.writerow(["Books", "Author", "Sales in Millions"]) # the first row that is being written is used to write the header of the file 

    csv_writer.writerow([best_selling_book[0], best_selling_book[1], best_selling_book[4]]) # then we are extracting the information from task one into each column in the new file that we created 

  
print("Bestselling information written to", output_file_path)

  













