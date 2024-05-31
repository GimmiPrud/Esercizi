
# Giammarco Prudenzi 
# Lezione sui Test 
i: int = 0
test_value: int = 0

assert i == 0  # assert viene utilizzato per verificare che una condizione sia True o False (test)
# inltre come il metodo raise anche assert può mandare un messaggio perzonalizzato di errore

# Esempi:
assert i == test_value, f" Error, the value i must be {test_value} instead is {i}"

def sum(a: int, b: int)-> int:

    return 0

result = sum(a=5,b=2)
test_value: int = 7
assert i == test_value, f" Error, the value i must be {test_value} instead is {i}"


