palabra1 ="vaca"
palabra2 = "perro" 

def comparar_longitud (palabra1,palabra2):
    longitud1 = len(palabra1)
    longitud2 = len(palabra2)
    return longitud1 == longitud2

resultado = comparar_longitud(palabra1,palabra2)

print(f"son {palabra1} y {palabra2} dos palabra con la misma longitud? = {resultado}")