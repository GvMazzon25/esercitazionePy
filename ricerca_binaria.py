# Lo scopo di questo esercizio è implementare un algoritmo di ricerca binaria

numeri_interi_ordinati = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 3

caratteri_alfabetici_ordinati = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
y = 'g'

nomi_ordinati = ['Alice', 'Bruno', 'Carla', 'Davide', 'Elena', 'Fabio', 'Giulia', 'Luca', 'Maria', 'Nico']
z = 'Fabio'

numeri_decimali_ordinati = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
w = 1.0


def search(lista, el, inizio=0, fine=None):
    if fine is None:
        fine = len(lista) - 1
    if inizio > fine:
        return -1

    punto_di_divisione = (inizio + fine) // 2
    element = lista[punto_di_divisione]

    if element == el:
        return punto_di_divisione
    elif el < element:
        return search(lista, el, inizio, punto_di_divisione - 1)
    else:
        return search(lista, el, punto_di_divisione + 1, fine)



def main():
    result = search(numeri_interi_ordinati, x)
    print(result)

    result = search(caratteri_alfabetici_ordinati, y)
    print(result)

    result = search(nomi_ordinati, z)
    print(result)

    result = search(numeri_decimali_ordinati, w)
    print(result)


if __name__ == '__main__':
    main()