# Calcolatore indice massa corporea (IMC)

# Calcola IMC
def calc_imc(peso, altezza):
    imc = peso / (altezza * altezza)
    return imc


# Seleziona la categoria
def select_categories(imc):
    if imc <= 18.5:
        return 'Sottopeso'
    elif 18.5 < imc <= 24.9:
        return 'Normopeso'
    elif 25 <= imc <= 29.9:
        return 'Sovrappeso'
    elif imc >= 30:
        return 'Obeso'


def is_number_and_dot(string):
    # Rimuovi tutti i punti dalla stringa
    temp_string = string.replace('.', '')
    # Controlla se tutti i caratteri rimanenti sono cifre
    return temp_string.isdigit()


def error_control(peso, altezza):
    if ',' in altezza:
        altezza = altezza.replace(',', '.')

    if is_number_and_dot(peso) and is_number_and_dot(altezza):
        peso = int(peso)
        altezza = float(altezza)
        imc = calc_imc(peso, altezza)
        result = select_categories(imc)
        return result
    else:
        error = 'Formato non corretto'
        return error


def main():
    while True:
        peso = input('Inserisci il tuo peso in KG: ')
        altezza = input('Inserisci la tua altezza: ')
        if peso == 'end' or altezza == 'end':
            return False
        else:
            result = error_control(peso, altezza)
            print(result)





main()
