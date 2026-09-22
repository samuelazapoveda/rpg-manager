def validar_personaje(nombre, clase, nivel, vida):
    opcion_valida = ("guerrero", "mago", "arquero")
    
    if nombre.strip() == "":
        return False  
        
    if clase not in opcion_valida:
        return False  
        
    if nivel < 1 or nivel > 100:
        return False  
        
    if vida < 1:
        return False  
        
    return True