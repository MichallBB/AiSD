#lab1 AiSD
def zad1(imie,nazwisko):
    return imie + ". " + nazwisko

print(zad1("M", "Bin"))

def zad2(imie,nazwisko):
    return imie[0].capitalize() + ". " + nazwisko.capitalize()

print(zad2("m", "bin"))

def zad3(first2, last2, age):
    return (int(f"{first2}{last2}"))-age

print(zad3(20,22,21))

def zad4(imie, nazwisko, funkcja):
    if funkcja=="zad2":
        return zad2(imie,nazwisko)
    elif funkcja=="zad1":
        return zad1(imie,nazwisko)
print(zad4("jan", "kowalski", "zad2"))

def zad5(liczba, dzielnik):
    if liczba!=0 and dzielnik!=0:
        return liczba/dzielnik
    return 0

print(zad5(2,0))


def zad6():
    suma = 0
    while suma<100:
        print("podaj liczbe: ")
        x = int(input())
        suma += x
    print(suma)

#zad6()

def zad7(lista):
    return tuple(lista)

print(zad7([1,2,3]))

def zad8():
    print("Jaka dlugosc ma miec krotka: ")
    ilosc = int(input())
    ile_jest = 0
    lista = []
    print("Podaj liczby: ")
    while ile_jest < ilosc:
        ile_jest += 1
        lista.append(input())
    print(tuple(lista))

#print(zad8())

def zad9(liczba):
    dni_tygodnia = {
        1: "Poniedzialek",
        2: "Wtorek",
        3: "Sroda",
        4: "Czwartek",
        5: "Piatek",
        6: "Sobota",
        7: "Niedziela",
    }
    return dni_tygodnia[liczba]
print(zad9(5))

def zad10(slowo):
    if slowo == slowo[::-1]:
        return 1
    return 0
print(zad10("kajsdak"))