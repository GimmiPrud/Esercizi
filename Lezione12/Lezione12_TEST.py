
# Giammarco Prudenzi 
# Lezione sui Test 
i: int = 0
test_value: int = 0

assert i == 0  # assert viene utilizzato per verificare una condizione  (test)
# inltre come il metodo raise anche assert può mandare un messaggio perzonalizzato di errore
# sintassi assert
# Esempi:
assert i == test_value, f" Error, the value i must be {test_value} instead is {i}"

def sum(a: int, b: int)-> int:

    return 0

result = sum(a=5,b=2)
test_value: int = 7
assert i == test_value, f" Error, the value i must be {test_value} instead is {i}"

# ci sono diversi tipi di assert che si trovano importando la libreria unittest{}







#---------------------------------------------------------------------------------------------------------------------#
# la funzine all() di python controlla se tutto quello che è all'interno di un object sia True 
# se tutto è true il risultato sarà true, se anche una sola condizione è false il risultato sarà false (tipo un and )
#---------------------------------------------------------------------------------------------------------------------#