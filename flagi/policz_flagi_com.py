from lista_flag import stworz_liste_flag

def policz_domeny_com(lista_flag):
    wynik = 0
    for flaga in lista_flag:
        if flaga[-4:] == '.com':
            wynik += 1
    return wynik

zrodlo_flag = 'https://zajecia-programowania-xd.pl/flagi'
lista_flag = stworz_liste_flag(zrodlo_flag)
wynik = policz_domeny_com(lista_flag)
print('Ilość domen .com na liście =', wynik)