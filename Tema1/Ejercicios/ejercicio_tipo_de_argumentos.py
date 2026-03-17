#luis enrique lopez zamora

def organizar_fiesta(invitados, tema="Python", lugar="aula de informática"):
    """
    Función que organiza una fiesta de cumpleaños.
    - invitados: argumento posicional (obligatorio)
    - tema: argumento de palabra clave con valor por defecto "Python"
    - lugar: argumento de palabra clave con valor por defecto "aula de informática"
    """
    print(f"Preparando una fiesta para {invitados} invitados.")
    print(f"Tema de la fiesta: {tema}")
    print(f"Lugar de la celebración: {lugar}")

print("\n\n")
print("--- Prueba 1: solo invitados ---\n\n")
organizar_fiesta(10)
print("\n\n")
print("--- Prueba 2: invitados y tema ---\n\n")
organizar_fiesta(10, tema="Fiesta de disfraces")
print("\n\n")
print("--- Prueba 3: invitados, tema y lugar ---\n\n")
organizar_fiesta(10, tema="Fiesta de disfraces", lugar="Salon de actos")