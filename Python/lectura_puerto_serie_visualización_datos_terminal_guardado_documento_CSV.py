import serial
import time
import math

nombre_archivo_sensores = "cansat1_sensores.csv"

port ='/dev/cu.usbserial-1410' #APC220
port_serie = serial.Serial(port, 9600)

if(port_serie.is_open):
    print(f"Connexión establecida a {port_serie.name}")

    with open(nombre_archivo_sensores, 'w') as file_object: #a afegeix al final i w sobreescriu el fitxer
        file_object.write("Paquete, Tiempo cansat, Equipo, Lectura termistor, Presión, Altitud BMP280, Temperatura BMP280, Lectura IR\n")

    print("Esperando datos:")

while True:
    if(port_serie.in_waiting > 0):
        lectura = port_serie.readline()
        lectura = lectura.decode('Ascii')
        lectura = lectura.rstrip("\r\n'")
        print(lectura)

        with open(nombre_archivo_sensores, 'a') as file_object:
            #file_object.write(f"{num_paquete},{tiempo_cansat},{nom_equipo},{lectura_termistor},{presion},{altitud_bmp280},{temperatura_bmp280},{lectura_ir}\n")
            file_object.write(f"{lectura}\n")

port_serie.close() # Tanca el port