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
        f.insert()

    elif choose == 2:
        f.show()

    elif choose == 3:
        f.analyze()

    else:
        print("Error")



if __name__ == '__main__':
    main()


