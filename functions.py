import sections as sc
import functions2 as f1

def insert():
    number = int(input("\nIndica el nombre d'alumnes que vols introduir: "))
    for i in range(number):
        f1.csv1()


def show():
        f1.csv2()

def analyze():
        records = input("\nQuants registres vol consultar?\na)El total dels registres\nb)Els primers registres\nc)Els darrers registres\n")
        if records == "a":
            sc.section1()
        elif records == "b":
            sc.section2()
        elif records == "c":
            sc.section3()
        else:
            print("Error")
