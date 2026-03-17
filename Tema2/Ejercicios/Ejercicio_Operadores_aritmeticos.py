def calcular_calorias(carbohidratos, proteinas, grasas):
    """
    Calcula las calorías totales a partir de los gramos de macronutrientes.
    
    Parámetros:
    carbohidratos (float o int): Gramos de carbohidratos.
    proteinas (float o int): Gramos de proteínas.
    grasas (float o int): Gramos de grasas.
    
    Retorna:
    float: Total de calorías.
    """
    calorias = (carbohidratos * 1) + (proteinas * 4) + (grasas * 9)
    return calorias


print("Luis Enrique Lopez Zamora \n\n")
print("---Ejercicio-Oper-Calorías ---")

ejemplo_calorias = calcular_calorias(30, 80, 7)
print(f"{ejemplo_calorias} calorías")