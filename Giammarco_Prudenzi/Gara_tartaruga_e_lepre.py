import random

pos_tarta = 1
pos_lepre = 1

def tartaruga(pos: int):

    mov_tartaruga: int = random.randint(1,10)

    if 1 <= mov_tartaruga <= 5:
        pos += 3
    elif 6 <= mov_tartaruga <=7:
        pos -= 6
        if pos < 1:
            pos = 1
    elif 8 <= mov_tartaruga <= 10:
        pos += 1
    
    return pos

def lepre(pos: int):

    mov_lepre: int = random.randint(1,10)

    if 1 <= mov_lepre <= 2:
        pos = pos
    elif 3 <= mov_lepre <= 4:
        pos += 9 
    elif mov_lepre == 5:
        pos -= 12
        if pos < 1:
            pos = 1
    elif 6 <= mov_lepre <= 8:
        pos += 1
    elif 9 <= mov_lepre <=10:
        pos -= 2
        if pos < 1:
            pos = 1

    return pos

def Gara(mov_tarta, mov_lepre):
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    while mov_lepre and mov_lepre < 70:
        mov_tarta = tartaruga(mov_tarta)
        mov_lepre = lepre(mov_lepre)
        circuito = [ "_" for n in range(1,70)]
        if mov_lepre == mov_tarta:
            circuito[mov_tarta] = "OUCH"
    return circuito
    
print(Gara())





