import math

lec_ter = float(input("Valor entre 0 y 1023 del termistor: "))
r_aux = 10 #kilohms

vol_ter = (5*lec_ter)/1023

r_ter = (vol_ter*r_aux)/(5-vol_ter)

t = round(73.74 - 21.06*math.log(r_ter),3)

print(f"La temperatura es {t} ºC")