#luis enrique lopez zamora

txt1 = "Nombre del planeta:"
txt2 = "Distancia al planeta:"
txt3 = "millones de km"

def planeta1():
    nombre = "neptuno"
    distancia = 58
    return nombre, distancia

def planeta2():
    nombre = "venus"
    distancia = 34
    return nombre, distancia

def planeta3():
    nombre = "tierra"
    distancia = 0
    return nombre, distancia

nombre, distancia = planeta1()
print(f"{txt1} {nombre}")
print(f"{txt2} {distancia} {txt3}\n")