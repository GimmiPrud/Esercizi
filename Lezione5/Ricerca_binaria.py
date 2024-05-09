# Giammarco Prudenzi

# Albero binario 
# ogni albero ha un nodo padre e dei nodi figli
# i nodi che stanno alla destra saranno sempre maggiori del nodo padre, mentre quelli alla sinistra saranno sempre più piccoli 

# Ricerca binaria:
# Quando si ha una lista (che deve essere ordinata) con molti elementi, si divide in due sotto liste e cosi via 
# questo è un metodo efficace per trovare un elemento all'interno della lista che contiene molti elementi

# Funzioni ricorsive (Ricorsive)

if False:
    
    def binary_search(array: list[int], x: int )-> int:
        return binary_search(array,x,0,len(array))

def binary_search(array: list[int], x: int, hight: int, low: int)->int:
    if low > hight:
        return None
    
    mid = (low + hight)//2
    if x == array[mid]:
        return mid
    else:
        if x > array[mid]:
            return binary_search(array,x,mid+1,hight)
        else:
            return binary_search(array,x,low,mid-1)
        
# Ricerca binaria iterativa:

def binary_search_iterative(array: list[int],x: int)-> int:
    low, hight = 0,len(array)
    while low < hight:
        mid = (low + hight)//2
        if x == array[mid]:
            return mid
        elif x > array[mid]:
            low = mid + 1
        else:
            hight = mid -1
# in caso di liste già ordinate conviene utilizzare i cicli 


        