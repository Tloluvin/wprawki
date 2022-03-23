TABLICA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def tablica(ile_wierszy, ile_kolumn):
    # ile_wierszy = 5
    # ile_kolumn = 6
    index = 0
    krok = 1
    wynik = ''
    przerywnik = ' '

    while ile_wierszy > 1:
        for index in TABLICA:
            if krok <= ile_kolumn:
                wynik += str(index) + przerywnik
                krok += 1
            else:
                krok = 2
                wynik += '\n'
                wynik += str(index) + przerywnik

                ile_wierszy -= 1
        # krok += 1
    return wynik


print(tablica(5, 6))
