
# Giammarco Prudenzi
# Quando le funzioni utilizzano come parametri altre funzionni (first class object)

# esempio:

def ciao(name: str)-> str:

    return f"Ciao {name}"

def salve(name: str)-> str:

    return f"Salve {name}"

def saluta_Dio(func)-> str:    # func si utilizza per far capire che utiliziamo una funzione come parametro di un altra 

    return func("Dio")


print(saluta_Dio(ciao))
print(saluta_Dio(salve))


# Funzioni innestate

def parent():   # le funzioni posso avere altre funzioni al loro interno (annidate)

    print("sono in parent")

    def first_child():             # first_child() e second_child() si trovano solo all'interno della funzione parent()

        print("first child ")

    def seconf_child():

        print("second child")

    seconf_child()
    seconf_child()
    first_child()


# Decorators (funzioni che ci permettono di andare a modificare il comportamento di un altra funzione)
# design pattern

def decorator(func):

    def wrapper():

        print("sono qui prima di func()")

        func()

        print("sonno qui dopo avre avviato la funzione func()")

    return wrapper
    
def ciao():

    print("ciao")

ciao()
ciao = decorator(ciao)
ciao()



# Esempio di decorator applicato al merge_sort (funzioni ricorsive):
# scrivere dei context manager utilizzando i decorator 

# Altro esempio di decorator:
class Analisi:

    @staticmethod
    def tempo(func):

        def wrapper(*args):
            import time

            start = time.time()

            value = func(*args)

            print(f"Time elapsed: {time.time() - start}")

            return value, time.time() - start
        
        return wrapper
    
@ Analisi.tempo
def area_cerchio(raggio: float):

    return raggio * raggio * 3.14

area_cerchio(1)


#---------------------------------------------------#
# Decorator
# @contextmanager(che fa parte della libreria di python contextlib):

def generatore():


    yield "A"
    yield "B"
    yield "C"

prova_generatore = generatore()

print(next(prova_generatore))
print(next(prova_generatore))
print(next(prova_generatore))
print(next(prova_generatore))

# ES. 

from contextlib import contextmanager

@contextmanager
def context_manager_decorator(*args):
    import time

    start_time: float = time.time()

    yield

    end_time: float = time.time()
    elapsed_time: float = end_time - start_time

    print(f"{elapsed_time=}")  # in questo modo viene richiamata comunque la variabile 

@ context_manager_decorator
def area_cerchio(raggio: float):

    return raggio * raggio * 3.14

#------------------------------------------------#

# Note --> (ogni processo ha un id diverso ed una zona di memoria diversa)
