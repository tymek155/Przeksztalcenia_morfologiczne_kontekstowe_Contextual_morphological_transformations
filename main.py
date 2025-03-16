from PIL import Image
import numpy as np

from read_txt import odczytaj_maske

number = 0

def wczytaj():
    image = Image.open("eevee.png").convert("L")
    to_bin = np.array(image)
    to_bin = binaryzacja(to_bin)
    return to_bin

def wczytaj_nobin():
    image = Image.open("eevee.png").convert("L")
    to_bin = np.array(image)
    #to_bin = binaryzacja(to_bin)
    return to_bin

def wczytaj_podst():
    image = Image.open("Mapa_MD_no_terrain_low_res_Gray.bmp").convert("L")
    to_bin = np.array(image)
    return to_bin

def binaryzacja(photo, a=100):
    for i in range(photo.shape[0]):
        for j in range(photo.shape[1]):
            if photo[i][j] <= a:
                photo[i][j] = 0
            else:
                photo[i][j] = 255
    return photo

def wyswietl(image):
    global number
    image = Image.fromarray(image)
    image.save("Zdjęcie"+str(number)+".jpg")
    image.show()
    number+=1

def dylatacja(image):
    x,y = image.shape
    edited = image.copy()

    for i in range(1, x-1):
        for j in range(1, y-1):
            if np.any(image[i-1:i+2, j-1:j+2] == 0):
                edited[i,j] = 0

    return edited


def erozja(image):
    x, y = image.shape
    edited = image.copy()

    for i in range(1, x - 1):
        for j in range(1, y - 1):
            if np.any(image[i - 1:i + 2, j - 1:j + 2] == 255):
                edited[i, j] = 255

    return edited

def rozmiar_maski(x):
    return (x-1)/2

def splot(image, r, maska):
    x,y = image.shape
    edited = image.copy()

    for i in range(r, x-r):
        for j in range(r, y-r):
            fragment = image[i-r:i+r+1, j-r:j+r+1]
            edited[i, j] = np.sum(fragment*maska)
            if edited[i, j] > 255:
                edited[i, j] = 255
            elif edited[i, j] < 0:
                edited[i, j] = 0

    return edited

def dylatacja_r(image, r):
    x, y = image.shape
    edited = image.copy()

    for i in range(r, x - r):
        for j in range(r, y - r):
            if np.any(image[i - r:i + r+1, j - r:j + r+1] == 0):
                edited[i, j] = 0

    return edited

def erozja_r(image, r):
    x, y = image.shape
    edited = image.copy()

    for i in range(r, x - r):
        for j in range(r, y - r):
            if np.any(image[i - r:i + r + 1, j - r:j + r + 1] == 255):
                edited[i, j] = 255

    return edited

def otw_morf(image, r):
    wynik = erozja_r(image, r)
    return dylatacja_r(wynik, r)

def domk_morf(image, r):
    wynik = dylatacja_r(image, r)
    return erozja_r(wynik, r)

def main():
    #Wczytanie maski z txt oraz promienia
    #maska = odczytaj_maske("upper_pass.txt")
    #r = rozmiar_maski(len(maska[0]))

    #Wczytanie zdjecia binarnie i w skali szarości
    image = wczytaj()
    image_nb = wczytaj_nobin()
    podst =wczytaj_podst()

    #wyswietl(image_nb)
    #wyswietl(image.copy())
    #wyswietl(dylatacja(image))
    #gauss = splot(image_nb, 1, np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]))
    #wyswietl(gauss)

    opt = 0
    opt2= 0
    while(opt != -1):
        print("1. Wyświetl oryginalne zdjęcie.")
        print("2. Wyświetl zdjęcie w formie binarnej.")
        print("3. Wykonaj dylatację.")
        print("4. Wykonaj erozję.")
        print("5. Wykonaj otwarcie morfologiczne.")
        print("6. Wykonaj domknięcie morfologiczne.")
        print("7. Wykonaj splot funkcji z maską.")
        print("8. Wczytaj zdjęcia ponownie.")
        print("-1. Wyjście")
        opt = int(input("Podaj wybraną opcję: "))

        if opt == 1:
            wyswietl(image_nb)
        elif opt == 2:
            wyswietl(image)
        elif opt == 3:
            rd = int(input('Podaj promień sąsiedztwa: '))
            image = dylatacja_r(image, rd)
            wyswietl(image)
        elif opt == 4:
            rd = int(input('Podaj promień sąsiedztwa: '))
            image = erozja_r(image, rd)
            wyswietl(image)
        elif opt == 5:
            rd = int(input('Podaj promień sąsiedztwa: '))
            image = otw_morf(image, rd)
            wyswietl(image)
        elif opt == 6:
            rd = int(input('Podaj promień sąsiedztwa: '))
            image = domk_morf(image, rd)
            wyswietl(image)
        elif opt == 7:
            while(opt2 != -1):
                print('\n1. Filtr Gaussa')
                print('2. Filtr low pass')
                print('3. Filtr upper pass')
                print('4. Filtr moj low pass')
                print('5. Filtr moj low pas na obrazie z lab 1')
                print('-1. Powrót')
                opt2 = int(input('Wybierz maskę: '))

                if opt2 == 1:
                    maska = odczytaj_maske("gauss.txt")
                    r = int(rozmiar_maski(len(maska[0])))
                    image_nb = splot(image_nb, r, maska)
                    wyswietl(image_nb)
                elif opt2 == 2:
                    maska = odczytaj_maske("low_pass.txt")
                    r = int(rozmiar_maski(len(maska[0])))
                    image_nb = splot(image_nb, r, maska)
                    wyswietl(image_nb)
                elif opt2 == 3:
                    maska = odczytaj_maske("upper_pass.txt")
                    r = int(rozmiar_maski(len(maska[0])))
                    image_nb = splot(image_nb, r, maska)
                    wyswietl(image_nb)
                elif opt2 == 4:
                    maska = odczytaj_maske("moj_low_pass.txt")
                    r = int(rozmiar_maski(len(maska[0])))
                    image_nb = splot(image_nb, r, maska)
                    wyswietl(image_nb)
                elif opt2 == 5:
                    maska = odczytaj_maske("moj_low_pass.txt")
                    r = int(rozmiar_maski(len(maska[0])))
                    podst = splot(podst, r, maska)
                    wyswietl(podst)
            opt2 = 0
        elif opt == 8:
            image = wczytaj()
            image_nb = wczytaj_nobin()
            podst = wczytaj_podst()


main()

#[[1/16,1/8,1/16],[1/8,1/4,1/8],[1/16,1/8,1/16]]
#[[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
#[[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]