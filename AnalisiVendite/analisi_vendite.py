# Immagina di lavorare per un'azienda che vende prodotti online.
# Hai ricevuto un file CSV contenente i dati delle vendite degli ultimi mesi.
# Il tuo compito è analizzare questi dati per fornire informazioni utili all'azienda
import pandas as pd
import matplotlib.pyplot as plt


# La funzione serve a ottenere i file dal csv
def csv_reader():
    # Percorso file CSV
    file_path = 'C:\\Users\\gvmaz\\OneDrive\\Desktop\\python\\ESERCIZI\\AnalisiVendite\\esempio_dati_vendite.csv'
    data = pd.read_csv(file_path)
    return data


# Centralina da cui partono le richieste per l'analisi dei dati
def data_analizer():
    data = csv_reader()
    id_prodotti = data['ID_Prodotto']
    prezzi_unitari = data['Prezzo_Unitario']
    quantities = data['Quantità']
    id_clienti = data['ID_Cliente']
    fatt = fatturato(prezzi_unitari, quantities)
    prodotto_magg = piu_venduto(quantities, id_prodotti)
    id_cliente = spesa_maggiore(quantities, prezzi_unitari, id_clienti)
    analisi = tendenza_vendita(data)
    print('id prodotto: ' + str(prodotto_magg))
    print('id Cliente con spesa maggiore: ' + str(id_cliente))
    return fatt


# Calcolo del fatturato
def fatturato(prezzi_unitari, quantities):
    somma = 0
    # Per ogni prezzo e quantità li moltiplica e somma i risultati insieme
    for i in range(len(prezzi_unitari)):
        prezzo_per_quantities = prezzi_unitari[i] * quantities[i]
        somma = somma + prezzo_per_quantities

    return round(somma, 2)


# Trova l'ID del prodotto più venduto
def piu_venduto(quantities, id_products):
    indice_maggiore = quantities.idxmax()
    prodotto = id_products[indice_maggiore]
    return prodotto


# Trova l'ID del cliente che ha speso di più
def spesa_maggiore(quantities, prezzi_unitari, id_clienti):
    list_spesa = list()
    for i in range(len(prezzi_unitari)):
        prezzo_per_quantities = prezzi_unitari[i] * quantities[i]
        list_spesa.append(prezzo_per_quantities)
    set_ordinato = sorted(list_spesa, reverse=True)
    # print(set_ordinato)
    max_spesa = set_ordinato[0]
    indx = list_spesa.index(max_spesa)
    id_cliente = id_clienti[indx]
    # print(id_cliente)
    return id_cliente


def tendenza_vendita(data):
    # Converti la colonna 'Data' in un formato di data
    data['Data'] = pd.to_datetime(data['Data'])
    # Estrai il mese
    data['Mese'] = data['Data'].dt.month
    # Calcola il fatturato per ogni vendita
    data['Fatturato'] = data['Prezzo_Unitario'] * data['Quantità']
    fatturato_per_mese = data.groupby('Mese')['Fatturato'].sum()
    #print(fatturato_per_mese)
    fatturato_per_mese.plot(kind='bar')
    plt.title('Fatturato Mensile')
    plt.xlabel('Mese')
    plt.ylabel('Fatturato')
    plt.show()


def main():
    result = data_analizer()
    print('fatturato azienda: ' + str(result) + ' $')


main()
