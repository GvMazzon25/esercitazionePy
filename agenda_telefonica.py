#Il tuo compito è creare una classe per un'agenda telefonica che permetta di gestire i contatti. Ogni contatto dovrebbe avere un nome, un cognome e un numero di telefono.

class Contatti:
    def __init__(self, nome, cognome, telefono):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono

    def numero_telefono(self):
        return f"{self.nome} {self.cognome}: {self.telefono}"


class Agenda:
    def __init__(self):
        self.elenco_contatti = []

    def aggiungi_contatto(self, contatto):
        self.elenco_contatti.append(contatto)

    def cerca_contatto(self, nome):
        contatti_trovati = []
        for contatto in self.elenco_contatti:
            if nome.lower() in contatto.nome.lower():
                contatti_trovati.append(contatto)
        return contatti_trovati

    def elimina_contatto(self, nome, cognome):
        contatto_eliminato = None
        for contatto in self.elenco_contatti:
            if nome.lower() in contatto.nome.lower() and cognome.lower() in contatto.cognome.lower():
                contatto_eliminato = contatto
                break
        if contatto_eliminato:
            self.elenco_contatti.remove(contatto_eliminato)
            print(f"Contatto {contatto_eliminato.nome} {contatto_eliminato.cognome} rimosso con successo.")


def main():
    print('ciao')