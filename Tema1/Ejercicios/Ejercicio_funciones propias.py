#Luis enrique lopez zamora

E1 = "Entero: 42, Tipo: <class 'int'>"
C1 = "Cadena: 42, Tipo: <class 'str'>"
F1 = "Flotante: 42.0, Tipo: <class 'float'>"

Frase = "Aprender Python es divertido"
Fr1 = len(Frase)
Numero = 10
NumeroT = Numero

def contar_caracteres():
    txt = f"La frase '{Frase}' tiene {Fr1} caracteres."
    return txt

def convertir_numero(num):

    entero = num
    cadena = str(num)
    flotante = float(num)
    resultado = (f"Entero: {entero}, Tipo: {type(entero)}\n"
                 f"Cadena: {cadena}, Tipo: {type(cadena)}\n"
                 f"Flotante: {flotante}, Tipo: {type(flotante)}")
    return resultado

print("\n\n")
print(contar_caracteres())
print("\n\n")
print("Conversiones del número "+ str(NumeroT) +":\n\n")
print(convertir_numero(Numero))
