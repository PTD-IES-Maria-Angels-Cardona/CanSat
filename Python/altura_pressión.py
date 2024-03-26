import math

#Datos invariables
g = 9.80866
m_aire = 0.0289644
r = 8.3144598
h_0 = 0
p_0 = 101300
t_0 = 13.2

p = float(input("Presión actual: ")) #La presión nos la dará el BMP280

h = h_0 + ((math.log(p_0/p)*r*t_0)/(g*m_aire)) #Formula de la altura

print(f"La altura es {h}") #Nos enseña la altura que hemos calculado