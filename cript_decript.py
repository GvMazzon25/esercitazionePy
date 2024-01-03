#Lo scopo di questo esercizio è scrivere due funzioni, una per criptare e una per decriptare un messaggio usando un semplice cifrario a sostituzione.
import random
lista_completa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

key1 = 2
key2 = 5


def cripta(messaggio, chiave):
    messaggio = list(messaggio)
    result = ''
    for i in messaggio:
        if i == ' ':
            new_char = random.randint(0,9)
            result = result + str(new_char)
        else:
            indexlist = lista_completa.index(i)
            new_index = indexlist + chiave
            len(lista_completa)
            if new_index > len(lista_completa):
                new_index = new_index - len(lista_completa)
                new_char = lista_completa[0 + new_index]
                result = result + str(new_char)
            else:
                new_char = lista_completa[indexlist + chiave]
                result = result + str(new_char)

    return result






def main():
    messaggio = input('Inserisci messaggio da criptare: ')
    print(cripta(messaggio, key1))


if __name__ == '__main__':
    main()