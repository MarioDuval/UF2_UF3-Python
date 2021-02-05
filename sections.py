import pandas    #importa la biblioteca pandas


def section1():     #funció per fer la primera opció que si lo dona al usuari que es per mostrar tots el registres
    try:
        df = pandas.read_csv('C:/Users/mario/PycharmProjects/UF2_UF3-Python/grades.csv')    #funció per llegir el fitxer
        print(df)       #es msotra per pantalla tots els registres
    except:
        print("Fitxer no trobat")


def section2():     #funció per fer la segona opció que si lo dona al usuari que es per mostrar els primers registres
    try:
        first = int(input("\nIntrodueix el nombre de registres que vols visualitzar: "))    #se li demana el nombre de registres que vol visualitzar
        df = pandas.read_csv('C:/Users/mario/PycharmProjects/UF2_UF3-Python/grades.csv')    #funció per llegir el fitxer
        print("\n", df.head(first))     #mostra per pantalla començant desde el principi del fitxer el nombre de registres indicats en la variable "first"
    except:
        print("Fitxer no trobat")

def section3():
    try:
        last = int(input("\nIntrodueix el nombre de registres que vols visualitzar: "))     #se li torna a demanar el nombre de registres que vol visualitzar
        df = pandas.read_csv('C:/Users/mario/PycharmProjects/UF2_UF3-Python/grades.csv')    #funció per llegir el fitxer
        print("\n", df.tail(last))      #mostra per pantalla començant desde el final del fitxer el nombre de registres indicats en la variable "last"
    except:
        print("Fitxer no trobat")