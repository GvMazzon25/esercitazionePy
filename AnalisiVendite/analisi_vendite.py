# Immagina di lavorare per un'azienda che vende prodotti online.
# Hai ricevuto un file CSV contenente i dati delle vendite degli ultimi mesi.
# Il tuo compito è analizzare questi dati per fornire informazioni utili all'azienda
import pandas as pd


# La funzione serve a ottenere i file dal csv
def csv_reader():
    # Percorso file CSV
    file_path = 'C:\\Users\\gvmaz\\OneDrive\\Desktop\\python\\ESERCIZI\\AnalisiVendite\\esempio_dati_vendite.csv'
    data = pd.read_csv(file_path)
    return data


# Calcolo del fatturato
def fatturato(data):
    somma = 0
    prezzi_unitari = data['Prezzo_Unitario']
    quantità = data['Quantità']
    #print(prezzi_unitari)
    #print(quantità)
    for i in range(len(prezzi_unitari)):
        prezzo_per_quantità = prezzi_unitari[i] * quantità[i]
        somma = somma + prezzo_per_quantità

    return somma


def main():
    data = csv_reader()
    fatt = fatturato(data)
    print(fatt)


main()
