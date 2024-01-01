# Immagina di lavorare per un'azienda che vende prodotti online.
# Hai ricevuto un file CSV contenente i dati delle vendite degli ultimi mesi.
# Il tuo compito è analizzare questi dati per fornire informazioni utili all'azienda
import pandas as pd
import matplotlib.pyplot as plt


# La funzione serve a ottenere i file dal csv
def csv_reader():
    # Percorso file CSV
    file_path = 'C:\\Users\\gvmaz\\OneDrive\\Desktop\\python\\ESERCIZI\\AnalisiVendite\\esempio_dati_vendite.csv'
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File non trovato.")
        return None


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
    tendenza_vendita(data)
    data_rapresentation(prodotto_magg,id_cliente,fatt)


def data_rapresentation(id_prodotto, id_cliente, fatturato):
    plt.figure(figsize=(8, 6))

    # Aggiunta del testo al grafico
    plt.text(0.5, 0.7, f"ID Prodotto: {id_prodotto}", horizontalalignment='center', fontsize=12)
    plt.text(0.5, 0.5, f"ID Cliente con Spesa Maggiore: {id_cliente}", horizontalalignment='center', fontsize=12)
    plt.text(0.5, 0.3, f"Fatturato Azienda: ${fatturato:.2f}", horizontalalignment='center', fontsize=12)

    # Impostazioni grafiche
    plt.axis('off')  # Nasconde gli assi
    plt.title("Scheda Informativa Aziendale", fontsize=16)

    # Visualizza il grafico
    plt.show()


# Calcolo del fatturato
def fatturato(prezzi_unitari, quantities):
    somma = (prezzi_unitari * quantities).sum()
    return round(somma, 2)


# Trova l'ID del prodotto più venduto
def piu_venduto(quantities, id_products):
    indice_maggiore = quantities.idxmax()
    prodotto = id_products[indice_maggiore]
    return prodotto


# Trova l'ID del cliente che ha speso di più
def spesa_maggiore(quantities, prezzi_unitari, id_clienti):
    # Converti liste in Series di pandas
    quantities_series = pd.Series(quantities)
    prezzi_unitari_series = pd.Series(prezzi_unitari)
    id_clienti_series = pd.Series(id_clienti)

    # Calcola la spesa totale per ogni cliente
    spesa_totale = quantities_series * prezzi_unitari_series

    # Trova l'indice della spesa massima
    indice_max_spesa = spesa_totale.idxmax()

    # Ottieni l'ID del cliente con la spesa massima
    id_cliente_max_spesa = id_clienti_series[indice_max_spesa]

    return id_cliente_max_spesa


def tendenza_vendita(data):
    # Converti la colonna 'Data' in un formato di data
    data['Data'] = pd.to_datetime(data['Data'])
    # Estrai il mese
    data['Mese'] = data['Data'].dt.month
    # Calcola il fatturato per ogni vendita
    data['Fatturato'] = data['Prezzo_Unitario'] * data['Quantità']
    fatturato_per_mese = data.groupby('Mese')['Fatturato'].sum()
    # print(fatturato_per_mese)
    fatturato_per_mese.plot(kind='bar')
    plt.title('Fatturato Mensile')
    plt.xlabel('Mese')
    plt.ylabel('Fatturato')
    plt.show()


def main():
    data_analizer()



if __name__ == '__main__':
    main()
