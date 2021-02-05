import functions as f

def main():
    print("*****************************************")
    print("********* Gestió d'alumnes **************")      #Benvinguda al programa
    print("*****************************************")


    print("\n1. Introduir alumnes.")        #menu de les opcions ques poden fer
    print("2. Mostrar alumnes.")
    print("3. Analitzar registres.")
    choose = int(input("\nQuina opció vols fer? "))     #variable on guardem el numero introduit per teclat indicant l'opció a fer

    if choose == 1:
        f.insert()      #crida a la funcio per introduir les dades

    elif choose == 2:
        f.show()        #crida a la funció per mostrar totes les dades del fitxer

    elif choose == 3:
        f.analyze()     #crida a la funció per analitzar els registres

    else:
        print("Opció incorrecte")



if __name__ == '__main__':
    main()


