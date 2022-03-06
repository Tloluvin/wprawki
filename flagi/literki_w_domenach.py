from lista_flag import stworz_liste_flag

szukana_litera = 'a'

def policz_literki(lista_flag):
    wynik = 0
    for flaga in lista_flag:
        ilosc = flaga.count(szukana_litera)
        wynik += ilosc
    return wynik

zrodlo_flag = 'https://zajecia-programowania-xd.pl/flagi'
lista_flag = stworz_liste_flag(zrodlo_flag)
wynik = policz_literki(lista_flag)
print(f"Ilość liter {szukana_litera} wynosi {wynik}")