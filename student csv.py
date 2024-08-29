#Program to write student data onto a csv file
#importing the csv module

import csv

#Field names
fields = ["Nmae", "Class", "Year", "Percent"]

#Data rows of csv file
rows = [["Rohit", "XII", "2003", "92"],
        ["Shaurya", "XI", "2004", "82"],
        ["Deep", "XII", "2002", "80"],
        ["Prerna", "XI", "2006", "85"],
        ["Lakshya", "XII", "2005", "72"]]

#Name of the csv file
filename="marks.csv"

#Writing to csv file
with open(filename, "w", newline="") as f:
    #By default, newline is '\r\n'
    #creating a csv writer object
    csv_w = csv.writer(f, delimiter = ",")
    #writing the fields (the column heading) once
    csv_w.writerow(fields)
    for i in rows:
        #writing the data row-wise
        csv_w.writerow(i)
    print("File Created")
