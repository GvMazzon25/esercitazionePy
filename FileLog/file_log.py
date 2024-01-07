# Immagina di avere un file di log di un'applicazione,
# dove ogni riga registra un evento con una data, un'ora e un messaggio di log.
# Il tuo compito è scrivere uno script Python per analizzare questo file di log e produrre un riassunto.

file_log = 'log.log'


def read_log():
    log_per_data = {}
    with open(file_log, 'r') as file:
        # leggo riga per riga
        for linea in file:
            data, messaggio = linea.split(' ', 1)
            data = data.strip()

            if data in log_per_data:
                log_per_data[data].append(messaggio.strip())
            else:
                log_per_data[data] = [messaggio.strip()]

    output_data = {}
    for data in log_per_data.keys():
        messaggi_per_data = log_per_data[data]
        numero_messaggi = len(messaggi_per_data)

        tupla = (numero_messaggi, messaggi_per_data)

        output_data[data] = tupla

    return output_data


def search_keyword(keyword, file_log):
    keyword_in_line = {}
    with open(file_log, 'r') as file:
        for line_number, line in enumerate(file, 1):  # Enumeriamo le linee e partiamo dalla riga 1
            if keyword in line:
                if keyword not in keyword_in_line:
                    keyword_in_line[keyword] = []  # Inizializziamo una lista vuota per la parola chiave
                keyword_in_line[keyword].append({'line_number': line_number, 'line_content': line.strip()})
    return keyword_in_line


def main():
    log_data = read_log()  # Ora otteniamo l'output dalla funzione
    for data, (numero_messaggi, messaggi_per_data) in log_data.items():
        print(f"Data: {data}, Numero di messaggi: {numero_messaggi}")
        for messaggio in messaggi_per_data:
            print(messaggio)
    print('--------')
    result = search_keyword('X',file_log)
    for keyword,lines in result.items():
        print(f"Parola chiave: {keyword}")
        for entry in lines:
            print(f"Riga {entry['line_number']}: {entry['line_content']}")


main()
