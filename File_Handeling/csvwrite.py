# csv - comma separated Values
import csv

studentData = [
    {"RollNo":101,"Name":"Ram","percentage":98},
    {"RollNo":102,"Name":"Shyam","percentage":50},
    {"RollNo":103,"Name":"Ravi","percentage":70},
    {"RollNo":104,"Name":"Rahul","percentage":100},
    {"RollNo":105,"Name":"Rakesh","percentage":40}
]

with open("data.csv",'w') as file:
    writer = csv.writer(file)
    for data in studentData:
        writer.writerow(data.values())

file.close()


