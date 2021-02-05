import csv      #importem la biblioteca csv
import os.path  #importem la biblioteca path


def csv1(): #funció per introduir els registres
    student_ID = int(input("Introdueix l'identificador: "))
    first_name = input("Introdueix el nom de l'estudiant: ")
    last_name = input("Introdueix el cognom de l'estudiant: ")      #variables on es demana que s'hi introdueixi les dades per teclat
    subject = input("Introdueix l'assignatura: ")
    grade = int(input("Introdueix la nota: "))

    student = {
        "student_ID": student_ID,
        "first_name": first_name,
        "last_name": last_name,             #estructura on guardem el que s'ha introduit per teclat
        "subject": subject,
        "grade": grade
    }
    file_exists = os.path.isfile('C:/Users/mario/PycharmProjects/UF2_UF3-Python/grades.csv')     #funció indicant que la variable es igual a la ruta on esta el fitxer
    fieldnames = ['student_ID', 'first_name', 'last_name', 'subject', 'grade']      #capçelera
    with open('C:/Users/mario/PycharmProjects/UF2_UF3-Python/grades.csv', 'a') as csvfile:      #s'obre el fitxer per afegir dades
        writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)       #per escriure al fitxer csv
        if not file_exists:     #condició per si el fitxer no existeix escrigui la capçelera
            writeCSV.writeheader()

        writeCSV.writerow(student)      #escriu per files el que s'ha introduit per teclat

def csv2():
    with open('C:/Users/mario/PycharmProjects/UF2_UF3-Python/grades.csv', encoding="utf8") as csvfile:      #s'obre el fitxer per llegir
        readCSV = csv.DictReader(csvfile, delimiter=',')

        for row in readCSV:     #bulce per recorrer tot el fitxer i mostri per pantalla les dades en files amb el delimitador ","
            print(f"{row['student_ID']}, {row['first_name']}, {row['last_name']}, {row['subject']}, {row['grade']}")