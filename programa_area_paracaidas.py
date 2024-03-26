#Clicad la flecha y id abajo para calcular el área.
import math #Sirve para utilitzar calculos como sin, cos o raiz quadrada.

missatge=" Calculador de área del paracaidas " #título
print("-"*(len(missatge)+2))
print("|"+missatge.upper()+"|")
print("-"*(len(missatge)+2))

print("""\nHola alumnado de TEX, este es nuestro programa
para calcular el área del paracaidas, si teneis alguna
duda enviad un correo, para escribir numeros decimales
escribe utilitzando el punto "." y solo tenies que poner el
numero, no poner la magnitud. Ejemplo: 0.1. """) #información sobre el programa

missatge=" Datos: " #título
print("")
print("-"*(len(missatge)+2))
print("|"+missatge.upper()+"|")
print("-"*(len(missatge)+2))

massa=float(input("\nEscribe la massa (g) del satélite: ")) #Para preguntar datos a los alumnos
v=float(input("Escribe la velocidad (m/s) del satélite: "))
n=int(input("Escribe el numero de lados que quiere tener el paracaidas: "))

massa /=1000 #Datos que no se pueden canviar
g=9.80655
c_f=0.8
d_a=1.225
rad=math.radians(180/n)

at=round(((2*massa*g)/(c_f*d_a*v**2))*10000) #Calculos para encontrar el área, el radio, la base i la altura.
r=round(math.sqrt((at)/(n*math.sin(rad)*math.cos(rad))),2)
b=round(2*r*math.sin(rad),2)
h=round(r*math.cos(rad),2)

missatge=" Resultados: " #título
print("")
print("-"*(len(missatge)+2))
print("|"+missatge.upper()+"|")
print("-"*(len(missatge)+2))
print(f"""\nÁrea total: {at} cm²
Radio: {r} cm
Velocidad: {v} m/s
Numero de lados: {n}
Distancia de los lados: {b} cm
Altura de los lados: {h} cm.""") #Mostramos los resultados a los alumnos