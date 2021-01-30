import pandas
import pandas as pd
import csv
import functions as f

def main():
    print("*****************************************")
    print("********* Gestió d'alumnes **************")
    print("*****************************************")


    print("\n1. Introduir alumnes.")
    print("2. Mostrar alumnes.")
    print("3. Analitzar registres.")
    choose = int(input("\nQuina opció vols fer? "))

    if choose == 1:
        number = int(input("\nIndica el nombre d'alumnes que vols introduir: "))
        for i in range(number):
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

            fieldnames = ['student_ID', 'first_name', 'last_name', 'subject', 'grade']
            with open('C:/Users/mario/PycharmProjects/UF2_UF3-Python/grades.csv', 'a') as csvfile:
                writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
                #writeCSV.writeheader()
                writeCSV.writerow(student)

    elif choose == 2:
        with open('C:/Users/mario/PycharmProjects/UF2_UF3-Python/grades.csv', encoding="utf8") as csvfile:
            readCSV = csv.DictReader(csvfile, delimiter=',')


            for row in readCSV:
                print(f"{row['student_ID']}, {row['first_name']}, {row['last_name']}, {row['subject']}, {row['grade']}")

    elif choose == 3:
        analyze = input("\nQuants registres vol consultar?\na)El total dels registres\nb)Els primers registres\nc)Els darrers registres\n")
        if analyze == "a":
            df = pandas.read_csv('C:/Users/mario/PycharmProjects/UF2_UF3-Python/grades.csv')
            print(df)
        elif analyze == "b":
            first = int(input("\nIntrodueix el número de registres que vols visualitzar: "))
            df = pd.read_csv('C:/Users/mario/PycharmProjects/UF2_UF3-Python/grades.csv')
            print("\n", df.head(first))

        elif analyze == "c":
            last = int(input("\nIntrodueix el número de registres que vols visualitzar: "))
            df = pd.read_csv('C:/Users/mario/PycharmProjects/UF2_UF3-Python/grades.csv')
            print("\n", df.tail(last))



if __name__ == '__main__':
    main()


