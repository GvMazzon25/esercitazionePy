def celsius_to_farenheit(celsius):
    farheneight = (celsius * 9 / 5) + 32
    return farheneight


def farenheit_to_celsius(farenheit):
    celsius = (farenheit - 32) * 5 / 9
    return celsius


def select_mode(user_input):
    F = ''
    C = ''
    #se nella parola è contenuto c di celsius viene selezionata la funzione celsius_to_farenheit
    if 'C' in user_input:
        number = user_input.replace('C', "")
        #stringa in numero
        c_num = int(number)
        #operazione
        F = celsius_to_farenheit(c_num)
        result = str(F) + 'F'
        #numero in stringa e aggiunta unità di misura
        return result
    # se nella parola è contenuto F di Farenheit viene selezionata la funzione farenheit_to_celsius
    elif 'F' in user_input:
        number = user_input.replace('F', "")
        # stringa in numero
        f_num = int(number)
        # operazione
        C = farenheit_to_celsius(f_num)
        # numero in stringa e aggiunta unità di misura
        result = str(C) + 'C'
        return result


def main():
    while True:
        user_input = input('Write temperature: ')
        if user_input == 'end':
            return False
        else:
            result = select_mode(user_input)
            print(result)


main()
