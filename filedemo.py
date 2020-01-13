import csv

total_records = 0
total_salary  = 0

with open("Z:/example.csv") as csvfile: 
    file = csv.reader(csvfile)

    for rec in file:
        total_records += 1
        print(f"{total_records} \t {rec[0]} \t {int(rec[2]):2.2f}")
        total_salary += int(rec[2])

print("TOTAL RECORDS: ", total_records)
print("TOTAL SALARY: ", total_salary)