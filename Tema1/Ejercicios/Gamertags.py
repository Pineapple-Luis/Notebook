def cabecera():
    """Muestra la cabecera de la aplicacion"""
    titulo = r""""
        ⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣠⣾⣿⣿⣿⣦⣄⡀⠀⠀⢀⣠⣴⣿⣿⣿⣷⣄⠀⠀⠀
    ⠀⠀⣼⣿⣿⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠉⣹⣿⣧⠀⠀
    ⠀⣼⣿⣉⣉⠀⣉⣙⣿⣿⣿⣿⣿⣿⣿⣟⠁⣹⣿⣏⠀⣹⣧⠀
    ⢠⣿⣿⣿⣿⣀⣿⣿⣿⣉⣉⣿⣿⣉⣹⣿⣿⣏⠀⣹⣿⣿⣿⡄
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⡇
    ⠸⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⠇
    ⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀
🎮!crea tu identidad gamertag¡🎮
    """  
    print(titulo)
cabecera()

#solicitar datos al usuario
nombre = input("\n introduce tu nombre:")
apellido = input("introduce tu apellido:")
numero_favorito = input("introduce tu numero favorito:")
print("\n")
print("\n================================")
print("\n🎮 TUS OPCIONES DE GAMETAG 🎮")
print("\n================================\n")

#funcion de tag basico
def crear_tag_basico(nombre):
    """
    Crea un gamertag basico usando la primeras 4 letras del nombre.

    Parametro:
    nombre(str): El nombre del usuario

    Retorna:
    str: Gamertag basico
    """

    tag= nombre[0:4]
    return tag
tag_basico = crear_tag_basico(nombre)
print("1. tag basico: "+tag_basico+"\n")

#funcion de tag invertido
def crear_tag_invertido(nombre):
    """
    Crear un gamer tag inertiendo el nombre completo

    parametro:
    str: El nombre del usuario

    Retorna:
    str: Gamertag (nombre) invertido
    """
    tag = nombre[::-1]
    return tag
tag_invertido = crear_tag_invertido(nombre)
print("2. tag invertido: "+tag_invertido+"\n")

#funcion de tag intercalado
def crear_tag_intercalado(nombre,apellido):
    """
    Crear un gamer tag intercalando el nombre completo

    parametro:
    str: El nombre del usuario
    str: El apellido de usuario

    Retorna:
    str: Gamertag (nombre) (apellido) intercalado
    """
    n1 = nombre[:1]
    a1 = apellido [:1]
    n2 = nombre[1:]
    a2 = apellido[1:]
    tag = n1+a2+n2+a2
    return tag
tag_intercalado = crear_tag_intercalado(nombre, apellido)
print("3. tag intercalado: "+tag_intercalado+"\n")

#funcion de tag elite
def crear_tag_elite(nombre):
    """
    Crear un gamer tag reduciendo el nombre completo

    parametro:
    str: El nombre del usuario

    Retorna:
    str: Gamertag (nombre) 2 primeras y 2 ultimas
    """
    n1 = nombre[:2]
    n2 = nombre[-2:]
    tag = n1+n2
    return tag
tag_elite = crear_tag_elite(nombre)
print("4. tag elite: "+tag_elite+"\n")

#funcion de tag con numero
def crear_tag_con_numero(nombre, numero_favorito):
    """
    Crear un gamer tag unido con el  y numero

    parametro:
    str: El nombre del usuario
    str: El numero favorito del usuario

    Retorna:
    str: Gamertag (nombre) (numero) unido
    """
    n1 = nombre[:4]
    tag = n1+ numero_favorito
    return tag
tag_con_numero = crear_tag_con_numero(nombre,str(numero_favorito))
print("5. tag con numero: "+tag_con_numero+"\n")

#funcion de estadisticas con el tag
def crear_tag_con_estadisticas(nombre):
    """
    Crear unas estadisticas del gamertag con tu nombre

    parametro:
    str: El nombre del usuario

    Retorna:
    str: Gamertag (nombre) nombre, la longitud de tu nombre,
    tu primera letra y ultima letra
    """
    n = nombre
    num = len(nombre)
    n1 = nombre[0]
    n2 = nombre[-1]
    return n,num,n1,n2
n,num,n1,n2 = crear_tag_con_estadisticas(nombre)
print("6.📊 ESTADÍSTICAS DE TU NOMBRE: ")
print("   1.Nombre completo: " + n)
print("   2.Longitud del nombre: " + str(num))
print("   3.Primera letra: " + n1)
print("   4.Última letra: " + n2)

print("\n🌟Elige tu favorito and GG🌟")