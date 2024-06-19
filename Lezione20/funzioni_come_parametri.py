
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


# Decorators (funzioni che ci permettono di andare a modificare il comportamento di un altra funzione )

