# Il tuo compito è creare una classe per un'agenda telefonica che permetta di gestire i contatti. Ogni contatto
# dovrebbe avere un nome, un cognome e un numero di telefono.


# Definizione della classe Contatti per rappresentare un singolo contatto
class Contatti:
    def __init__(self, nome, cognome, telefono):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono

    def numero_telefono(self):
        return f"{self.nome} {self.cognome}: {self.telefono}"


# Definizione della classe AgendaTelefonica per gestire una lista di contatti
class AgendaTelefonica:
    def __init__(self):
        self.elenco_contatti = []

    def mostra_contatti(self):
        for contatto in self.elenco_contatti:
            print(str(contatto.numero_telefono()))

    def aggiungi_contatto(self, contatto):
        self.elenco_contatti.append(contatto)
        print('Contatto creato con successo')

    def cerca_contatto(self, nome):
        contatti_trovati = []
        for contatto in self.elenco_contatti:
            if nome.lower() in contatto.nome.lower():
                contatti_trovati.append(contatto)
                print('Contatto trovato con successo')
            else:
                break
        if not contatti_trovati:
            print(error())
        else:
            return contatti_trovati

    def elimina_contatto(self, nome, cognome):
        contatto_eliminato = None
        for contatto in self.elenco_contatti:
            if nome.lower() in contatto.nome.lower() and cognome.lower() in contatto.cognome.lower():
                contatto_eliminato = contatto
        if contatto_eliminato:
            self.elenco_contatti.remove(contatto_eliminato)
            print(f"Contatto {contatto_eliminato.nome} {contatto_eliminato.cognome} rimosso con successo.")
        else:
            print(error())


# Funzione per gestire eventuali errori (attualmente non utilizzata)
def error():
    message = 'Not Found'
    return message


# Funzione principale
def main():
    # Creazione di un'istanza di AgendaTelefonica
    agenda = AgendaTelefonica()

    # Creazione di alcuni contatti e aggiunta all'agenda telefonica
    contatto1 = Contatti("Mario", "Rossi", "1234567890")
    contatto2 = Contatti("Luigi", "Verdi", "9876543210")
    contatto3 = Contatti("Anna", "Bianchi", "5555555555")

    agenda.aggiungi_contatto(contatto1)
    agenda.aggiungi_contatto(contatto2)
    agenda.aggiungi_contatto(contatto3)
    print('-----------')
    # Cerco contatto
    agenda.cerca_contatto('Mario')
    agenda.cerca_contatto('Giorgio')  # Not Found
    print('-----------')
    # Eliminazione di un contatto
    agenda.elimina_contatto("Mario", "Rossi")
    agenda.elimina_contatto("Giorgio", 'Mazzon')  # Not Found
    print('-----------')
    # Visualizzazione dei contatti rimanenti nell'agenda telefonica
    agenda.mostra_contatti()


if __name__ == '__main__':
    main()
