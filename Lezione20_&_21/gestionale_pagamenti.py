
# Giammarco Prudenzi 

# GESTIONALE PAGAMENTO
'''
Si definisca una nuova classe Pagamento
che contiene un attributo privato e di tipo float che memorizza l'importo del pagamento e si definiscano appropriati metodi get() e set().
L'importo non è un parametro da passare in input alla classe Pagamento ma deve essere inizializzato utilizzando il metodo set() dove opportuno.
Si crei inoltre un metodo dettagliPagamento() che visualizza una frase che descrive l'importo del pagamento,
ad esempio: "Importo del pagamento: €20.00". Quando viene stampato, l'importo è sempre con 2 cifre decimali.

Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo.
Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti.
Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o 
in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per pagare l'importo in contanti.

Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. 
Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, e il numero della carta di credito.
Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte le informazioni della carta di credito oltre all'importo del pagamento.

Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito con valori differenti
e si invochi dettagliPagamento() per ognuno di essi.

Esempio di output:
Pagamento in contanti di: €150.00
150.00 euro da pagare in contanti con:
1 banconota da 100 euro
1 banconota da 50 euro

Pagamento in contanti di: €95.25
95.25 euro da pagare in contanti con:
1 banconota da 50 euro
2 banconote da 20 euro
1 banconota da 5 euro
1 moneta da 0.2 euro
1 moneta da 0.05 euro

Pagamento di: €200.00 effettuato con la carta di credito
Nome sulla carta: Mario Rossi
Data di scadenza: 12/24
Numero della carta: 1234567890123456

Pagamento di: €500.00 effettuato con la carta di credito
Nome sulla carta: Luigi Bianchi
Data di scadenza: 01/25
Numero della carta: 6543210987654321
'''
# Svolgimento:

class Pagamento:

    def __init__(self):
        self.__importo_pagamento: float = None
    
    def set_pagamento(self, importo: float):
        self.__importo_pagamento = importo

    def get_pagamento(self):
        return self.__importo_pagamento

    def dettagli_Pagamento(self):
        return f" pagamento di £{self.__importo_pagamento}"


class PagamentoContanti(Pagamento):
    def __init__(self):
        super().__init__()
    
    def dettagli_Pagamento(self):
        return f"{super().dettagli_Pagamento()} in contanti"

    def inPezziDa(self):
        importo = self.get_pagamento()
        tagli = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.01]
        for taglio in tagli: 
            if taglio < 5:
                print(f"{importo//taglio} monete da {taglio} euro ")
                importo = importo%taglio
            else:
                print(f"{importo//taglio} banconote da {taglio} euro ")
                importo = importo%taglio


class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, nome_titolare_carta: str, data_scadenza: str, numero_carta_credito: str):
        super().__init__()
        self.nome_titolare_carta = nome_titolare_carta
        self.data_scadenza = data_scadenza
        self.numero_carta_credito = numero_carta_credito
    
    
    def dettagli_Pagamento(self):
        if len(self.numero_carta_credito) == 16:
            return f"{super().dettagli_Pagamento()} effettuato con la carta di credito\n Nome sulla carta: {self.nome_titolare_carta}\n Data di scadenza: {self.data_scadenza}\n Numero della carta: {self.numero_carta_credito}"
        else:
            return "numero carta di credito non valida"
