import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    with open("packing_list.csv", "r") as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            print(row)


except FileNotFoundError:
    print("Packing list file not found. Create a new one")

    with open("packing_list.csv", "w") as file:
        csv_writer = csv.writer(file)

        csv_writer.writerows(data) # it needs to be plural. .writerows. not .writerow

        
