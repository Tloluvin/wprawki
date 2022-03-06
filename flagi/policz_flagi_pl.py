from lista_flag import stworz_liste_flag

def policz_domeny_pl(lista_flag):
    wynik = 0
    for flaga in lista_flag:
        if '.pl' in flaga:
            wynik += 1
    return wynik

zrodlo_flag = 'https://zajecia-programowania-xd.pl/flagi'
lista_flag = stworz_liste_flag(zrodlo_flag)
wynik = policz_domeny_pl(lista_flag)
print('ilość flag w domenach .pl = ', wynik)