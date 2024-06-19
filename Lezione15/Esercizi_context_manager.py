
# Giammarco Prudenzi
# Esercizi context manager 

# Esercizio 1 & 2:
'''
Crea un context manager usando una classe
Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.
Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__
Esempio di funzionamento:
Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.
with FileManager('example.txt', 'w') as f:

    f.write('Hello, world!')

Crea un context manager che permette di calcolare il tempo che viene impiegato ad eseguire le istruzioni che si trovano nel with
with Timer():

    time.sleep(1)
time elapsed: 1.00000
in questo esempio il tempo passato non sarà mai uguale a 1
'''
# Svolgimento ES. 1 & 2:

class FileManager:

    def __init__(self, file_name: str, mode: str):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.filewrapper = open(self.file_name, self.mode)
        return self.filewrapper

    def __exit__(self, exc_type, exc_value, traceback):
        self.filewrapper.close()


with FileManager(file_name= "prova.txt",mode= "W") as file:
    file.write("pensala un altra")

with open("prova.txt","a"):
    file.write("Pensala un altra ")

class Timer:

    def __enter__(self):
        import time

        self.time = time.time()

    def __exit__(self):
        import time

        print(f"Time Elapsed: {time.time() - self.time}")

        return False