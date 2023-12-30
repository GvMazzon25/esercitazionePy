# Calcolatore indice massa corporea (IMC)

#Calcola IMC
def calc_imc(peso, altezza):
    peso = int(peso)      
    altezza = float(altezza)
    imc = peso / (altezza * altezza)
    return imc

#Seleziona la categoria
def select_categories(imc):
    if imc <= 18.5:
        return 'Sottopeso'
    elif 18.5 < imc <= 24.9:
        return 'Normopeso'
    elif 25 <= imc <= 29.9:
        return 'Sovrappeso'
    elif imc >= 30:
        return 'Obeso'


def main():
    peso = input('Inserisci il tuo peso in KG: ')
    altezza = input('Inserisci la tua altezza: ')
    imc = calc_imc(peso, altezza)
    result = select_categories(imc)
    print(result)


main()
