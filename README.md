Go to [English version](#english-version)
# Ogólne informacje
Projekt realizuje implementacje konsolowej aplikacji do przetwarzania obrazów 
za pomocą operacji morfologicznych/kontekstowych, filtrów splotowych. Obrazy są 
wczytywane w skali szarości, mogą być binaryzowane, można dokonywać na nich 
operacji morfologicznych (dylatacja, erozja, otwarcie oraz domknięcie) z doborem 
promienia sąsiedztwa, możliwy jest także także splot z różnego rodzajami mask 
(możliwość wczytania maski z pliku tekstowego). Wyniki mogą być zapisywane do 
plików .jpg.

# Technologie
W kodzie użyto:
* Python 3.12
* NumPy 2.2.2
* Pillow 11.0.0
	
# Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Kod podzielony jest między 
dwa pliki: `main.py` oraz `read_txt.py`. Pierwszy plik składa sie z funkcji 
`wczytaj`, `wczytaj_nobin`, `wczytaj_podst`, służących do ładowania obrazów, 
`binaryzacja` konwertującej plik do obrazu binarnego, `dylatacja_r` służącej do 
operacji dylatacji z zadanym promieniem, `erozja_r` służacej do operacji erozji 
z zadanym promieniem, `splot` aplikującej maskę splotową na obraz, w funkcji 
głównej `main` zaprojektowane jest całe menu konsolowe służące do wyświetlania 
obrazu oryginalnego/binarnego, wykonania dylatacji/erozji z zadanym promieniem 
oraz zastosowania wybranych filtrów. W drugim pliku zaporjektowana jest funkcja 
`wczytaj_maske` służąca do wczytywania masek splotowych z plików tekstowych, wraz 
z konwersją do wartości liczbowych.

## Oryginalne zdjęcie
![image](https://github.com/user-attachments/assets/ea0cfe74-9251-4229-a510-22e3085d634c)

## Zdjęcie po dylatacji z promieniem 5
![image](https://github.com/user-attachments/assets/0c35ffcf-0e25-4c07-a1a3-3a0ee011e2f3)

## Zdjęcie po erozji z promieniem 2
![image](https://github.com/user-attachments/assets/1cd32f1a-c3a2-4a11-97e2-7f356c485322)

## Zdjęcie po otwarciu morfologicznym z promieniem 2
![image](https://github.com/user-attachments/assets/f9dc4968-8b28-4297-b722-bb45edef126b)

## Zdjęcie po domknięciu morfologicznym z promieniem 4
![image](https://github.com/user-attachments/assets/9476085e-d4b8-4ba8-8dc3-0c94825fb8a8)

## Zdjęcie z filtrem low pass
![image](https://github.com/user-attachments/assets/726619b0-6149-48b9-953e-0224bb8e3b73)


# English version

# General Information  
The project implements a console application for image processing using 
morphological/contextual operations and convolutional filters. Images are 
loaded in grayscale, can be binarized, and undergo morphological operations 
(dilation, erosion, opening, closing) with adjustable neighborhood radius. 
Additionally, convolution with various mask types is supported (including 
loading masks from text files). Results can be saved to `.jpg` files.  

# Technologies  
The code uses:  
* Python 3.12
* NumPy 2.2.2
* Pillow 11.0.0 

# Usage  
The code was run and written in the PyCharm environment. The code is divided 
into two files `main.py` and `read_txt.py`. The first file consists of the 
functions `wczytaj`, `wczytaj_nobin`, `wczytaj_podst`** for loading images, 
`binaryzacja` converting the file to a binary image, `dylatacja_r` for 
performing dilation operations with a specified radius, `erozja_r` for 
performing erosion operations with a specified radius, `splot` applying a 
convolution mask to the image, the `main` function contains the entire 
console menu designed for displaying original/binary images, executing 
dilation/erosion with a specified radius, and applying selected filters. In the 
second file, the `wczytaj_maske` function is implemented for loading convolution 
masks from text files, including conversion to numerical values.  

## Original photo
![image](https://github.com/user-attachments/assets/ea0cfe74-9251-4229-a510-22e3085d634c)

## Photo after dilatation with radius 5
![image](https://github.com/user-attachments/assets/0c35ffcf-0e25-4c07-a1a3-3a0ee011e2f3)

## Photo after erosion with radius 2
![image](https://github.com/user-attachments/assets/1cd32f1a-c3a2-4a11-97e2-7f356c485322)

## Photo after morphological opening with radius 2
![image](https://github.com/user-attachments/assets/f9dc4968-8b28-4297-b722-bb45edef126b)

## Photo after morphological closure with radius 4
![image](https://github.com/user-attachments/assets/9476085e-d4b8-4ba8-8dc3-0c94825fb8a8)

## Photo with low pass filter
![image](https://github.com/user-attachments/assets/726619b0-6149-48b9-953e-0224bb8e3b73)
