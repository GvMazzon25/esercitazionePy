# Creare un programma Python che generi una password casuale
import random

maiusc = ('A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z')
minusc = ('a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
num = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
special = ('!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@','[', ']','^', '_', '{', '|', '}', '~')

#Unisce tutti i set e sceglie un carattere randomico da esso
def char_selector():
    set = maiusc + minusc + num + special
    return random.choice(set)

#Ottiene la lunghezza della password in input e aggiunge il carattere alla stringa password quante volte è richiesto dall'utente
def password_builder(password_lenght):
    password = ''
    for i in range(password_lenght):
        char = char_selector()
        password = password + char
    print(password)

#Ottiene l'input dall'utente (la lunghezza della password)
def user_input():
    while True:
        user = input("Inserisci lunghezza password: ")
        if user.isdigit():
            return int(user)
        else:
            print('Errore: inserisci un numero')


def main():
    password_lenght = user_input()
    password_builder(password_lenght)


main()
