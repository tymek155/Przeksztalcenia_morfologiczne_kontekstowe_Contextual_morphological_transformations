from fractions import Fraction

def odczytaj_maske(filename):
    with open(filename, 'r') as file:
        macierz = []
        for linia in file:
            wiersz = [float(Fraction(liczba)) for liczba in linia.split()]
            macierz.append(wiersz)
    return macierz