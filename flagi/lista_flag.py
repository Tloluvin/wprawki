import requests
import sys


def pobierz_strone_www_jako_text(dane_z_flagami):
    # Pobranie tekstu ze strony (jako tafla tesktu).
    surowe_info = requests.get(dane_z_flagami)
    text = surowe_info.text
    return text


def stworz_liste_flag(dane_z_flagami):
    '''
    Zamienia tekst ze strony na liste flag.
    '''

    text_strony_www = pobierz_strone_www_jako_text(dane_z_flagami)
    lista_linii = text_strony_www.split('</p>')
    linki = []
    # Iteruje po wszystkich fragmentach tekstu z html
    # i dodaje do listy tylko te ktore maja link url.
    for linia in lista_linii:

        link = linia.replace('<p>', '')
        link = link.replace('- ', '')
        # link = link.replace()
        link = link.strip()
        if ' ' in link or '<' in link:
            continue
        linki.append(link)

    return linki




# if __name__ == '__main__':
#     argument = sys.argv[1]
#     lista_flag = stworz_liste_flag(argument)
# print(lista_flag)
