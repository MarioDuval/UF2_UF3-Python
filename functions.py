import sections as sc       #importem el fitxer de funcions de l'arxiu sections on tenim els pandas
import functions2 as f1     #importem el fitxer de funcions de l'arxiu sections on tenim els csv's

def insert():   #funció per introduir dades
    number = int(input("\nIndica el nombre d'alumnes que vols introduir: "))    #variable on l'usuari introdueix per teclat el alumnes que vol introduir
    for i in range(number):     #bucle on li diem que mentre i no sigui el numero que ha introduit l'usuari no finalitzi
        f1.csv1()               #crida a la funció de csv per introduir les dades


def show():     #funció per mostrar dades
        f1.csv2()           #crida a la funció de csv per mostrar les dades

def analyze():  #funció per analitzar dades
        records = input("\nQuants registres vol consultar?\na)El total dels registres\nb)Els primers registres\nc)Els darrers registres\n")     #Consultem a l'usuari quants registres vol consultar i li donem opcions
        if records == "a":      #estructura de selecció per escollir l'opció que es vol realitzar
            sc.section1()       #crida a la funció del pandas per mostrar tots el registres
        elif records == "b":
            sc.section2()       #crida a la funció del pandas per mostrar els primers registres
        elif records == "c":
            sc.section3()       #crida a la funció del pandas per mostrar els últims registres
        else:
            print("Opcion incorrecta")
