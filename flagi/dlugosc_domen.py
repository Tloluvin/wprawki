from lista_flag import stworz_liste_flag
def dlugosc_domen(lista_flag):
    wynik = ['najkrótsza', 'najdłuższa']
    min_dlugosc = 1000
    max_dlugosc = 0
    for flaga in lista_flag:
        if (len(flaga) < min_dlugosc) and (len(flaga) > 0):
            min_dlugosc = len(flaga)
            wynik[0] = flaga
        if len(flaga) > max_dlugosc:
            max_dlugosc = len(flaga)
            wynik[1] = flaga
    return wynik

zrodlo_flag = 'https://zajecia-programowania-xd.pl/flagi'
lista_flag = stworz_liste_flag(zrodlo_flag)
wynik = dlugosc_domen(lista_flag)
print(f"Najdłuższa domena to {wynik[0]}, najkrótsza domena to {wynik[1]}")