import csv
import os.path


def csv1():
    student_ID = int(input("Introdueix l'identificador: "))
    first_name = input("Introdueix el nom de l'estudiant: ")
    last_name = input("Introdueix el cognom de l'estudiant: ")
    subject = input("Introdueix l'assignatura: ")
    grade = int(input("Introdueix la nota: "))

    student = {
        "student_ID": student_ID,
        "first_name": first_name,
        "last_name": last_name,
        "subject": subject,
        "grade": grade
    }
    file_exists = os.path.isfile('C:/Users/mario/PycharmProjects/UF2_UF3-Python/grades.csv')
    fieldnames = ['student_ID', 'first_name', 'last_name', 'subject', 'grade']
    with open('C:/Users/mario/PycharmProjects/UF2_UF3-Python/grades.csv', 'a') as csvfile:
        writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writeCSV.writeheader()

        writeCSV.writerow(student)

def csv2():
    with open('C:/Users/mario/PycharmProjects/UF2_UF3-Python/grades.csv', encoding="utf8") as csvfile:
        readCSV = csv.DictReader(csvfile, delimiter=',')

        for row in readCSV:
            print(f"{row['student_ID']}, {row['first_name']}, {row['last_name']}, {row['subject']}, {row['grade']}")