
# Giammarco Prudenzi 

reader = print(open("Lezione15/esempio.txt", encoding="utf-8"))      # ci sono diversi encoding(UTF8, UTF7, UTF16, UTF32 ,ASCII) e si utilizzano come tipi di codifica dei caratteri 
                                                                     # ci sono delle differenze tra l'utilizzo dei diversi encoding(come per esempio l'utilizzo di bit per la scrittura dei caratteri o i caratteri contenuti)

with open("Lezione15/esempio.txt") as reader:
    print(reader)

try:

    reader.readline()
    print("sono nella try")
    raise Exception("Eccezionale!")

except Exception:

    print("sono nella except")

finally:

    print("sono nella finally")
    reader.close()



