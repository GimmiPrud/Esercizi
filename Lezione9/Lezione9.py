# Giammarco Prudenzi 

# Ripasso classi ed introduzione delle keyword args (kwargs)

def nome_funzione(arg_1: int, **kwarg): # si utilizzano per passare qualsiasi argomento (parametri arbitrari) e creare un dizionario 

    alpha: float = kwarg["alpha"] # permette di creare altri argomenti senza aggiungerli nella funzione 

def complex_statistical_function(x, distribution_type, **kwargs):
    if distribution_type == "geometric":

        p: float = kwargs["p"]
    
    elif distribution_type == "poisson":

        lambda_1: float = kwargs["lambda_1"] 