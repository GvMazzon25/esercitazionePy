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

#Centralina da cui partono le richieste per l'analisi dei dati
def data_analizer():
    data = csv_reader()
    fatt = fatturato(data)
    maggiore = piu_venduto(data)
    print(maggiore)
    return fatt


# Calcolo del fatturato
def fatturato(data):
    somma = 0
    prezzi_unitari = data['Prezzo_Unitario']
    quantità = data['Quantità']
    #Per ogni prezzo e quantità li moltiplica e somma i risultati insieme
    for i in range(len(prezzi_unitari)):
        prezzo_per_quantità = prezzi_unitari[i] * quantità[i]
        somma = somma + prezzo_per_quantità

    return somma

def piu_venduto(data):
    quantità = data['Quantità']
    maggiore = max(quantità)
    indice_maggiore = quantità.idxmax()
    #print(indice_maggiore)
    id_products = data['ID_Prodotto']
    prodotto = id_products[indice_maggiore]
    return prodotto

def spesa_maggiore():
    print('ciao')


def main():
    result = data_analizer()
    print(result)


main()
