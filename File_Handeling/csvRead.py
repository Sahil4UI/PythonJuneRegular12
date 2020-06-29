import csv

students = []
# file = open('data.csv','r')
with open('data.csv','r') as file:
    reader = csv.reader(file)
    for data in reader:
        student = {"RollNo":data[0],"Name":data[1],"Percentage":data[2]}
        students.append(student)
print(students)
file.close()        
