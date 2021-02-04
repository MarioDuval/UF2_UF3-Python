import pandas


def section1():
    df = pandas.read_csv('C:/Users/mario/PycharmProjects/UF2_UF3-Python/grades.csv')
    print(df)


def section2():
    first = int(input("\nIntrodueix el número de registres que vols visualitzar: "))
    df = pandas.read_csv('C:/Users/mario/PycharmProjects/UF2_UF3-Python/grades.csv')
    print("\n", df.head(first))


def section3():
    last = int(input("\nIntrodueix el número de registres que vols visualitzar: "))
    df = pandas.read_csv('C:/Users/mario/PycharmProjects/UF2_UF3-Python/grades.csv')
    print("\n", df.tail(last))