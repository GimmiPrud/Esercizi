
def info_car(manufacture: str, model_name: str, **build):
    
    build["manufacture"] = manufacture
    build["model_name"] = model_name
    return build 


