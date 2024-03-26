lectura = "1, 1120, alicia sintes, 1, 101325.34, 100.32, 20.5, 0" #ejemplo

datos = lectura.split(", ") #separamos los datos

# Guardamos datos en variables
num_paquete = datos[0]
tiempo_cansat = datos[1]
nombre_equipo = datos[2]
lectura_termistor = int(datos[3])
presion = float(datos[4])
altitud_bmp280 = float(datos[5])
temperatura_bmp280 = float(datos[6])
lectura_ir = int(datos[7])