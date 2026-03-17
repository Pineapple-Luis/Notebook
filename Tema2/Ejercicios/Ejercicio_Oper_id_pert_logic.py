#Luis Enrique Lopez Zamora

palabra_adivinar = "Perro"
letra_prueba = "P"
palabra_intento = input("\n introduce tu palabra:")


def adivinar_palabra(letra_prueba, palabra_intento):

    letra_en_palabra = letra_prueba in palabra_adivinar
    print(f"¿La letra de prueba se encuentra en la palabra? {letra_en_palabra}")

    resultado_adivinanza = (palabra_intento == palabra_adivinar) and (len(palabra_intento) == len(palabra_adivinar))
    print(f"El jugador gana: {resultado_adivinanza}")

adivinar_palabra(letra_prueba, palabra_intento)