# Lo scopo di questo esercizio è scrivere due funzioni, una per criptare e una per decriptare un messaggio usando un semplice cifrario a sostituzione.
import random

lista_completa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
num_list = ['0','1','2','3','4','5','6','7','8','9']

key1 = 2
key2 = 5

#Funzione per criptare il messaggio
def cripta(messaggio, chiave):
    messaggio = list(messaggio)
    result = ''
    #Ciclo sul messaggio
    for i in messaggio:
        #Se trova uno spazio lo sostituisce con un numero casuale
        if i == ' ':
            new_char = random.randint(0, 9)
            result = result + str(new_char)
        else:
            indexlist = lista_completa.index(i)
            new_index = (indexlist + chiave)
            #Se il nuovo indice è troppo grande per la lista delle lettere l'indice torna a zero e viene sommato il resto della chiave
            if new_index > len(lista_completa):
                new_index = new_index - len(lista_completa)
                new_char = lista_completa[0 + new_index]
                result = result + str(new_char)
            else:
                new_char = lista_completa[indexlist + chiave]
                result = result + str(new_char)

    return result

#Funzione per decriptare il messaggio
def decript(messaggio, chiave):
    messaggio = list(messaggio)
    result = ''
    # Ciclo sul messaggio
    for i in messaggio:
        # Se trova un numero lo sostituisce con uno spazio
        if i in num_list:
            new_char = ' '
            result = result + str(new_char)
        else:
            indexlist = lista_completa.index(i)
            new_index = (indexlist + chiave)
            # Se il nuovo indice è negativo l'indice torna all'indice massimo e viene sottratto il resto della chiave
            if new_index < 0:
                new_index = len(lista_completa) - abs(new_index)
                new_char = lista_completa[new_index]
                result = result + str(new_char)
            else:
                new_char = lista_completa[indexlist - chiave]
                result = result + str(new_char)

    return result


def main():
    messaggio = input('Inserisci messaggio da criptare: ')
    prova1 = cripta(messaggio, key1)
    print(prova1)
    prova2 = decript(prova1, key1)
    print(prova2)


if __name__ == '__main__':
    main()
