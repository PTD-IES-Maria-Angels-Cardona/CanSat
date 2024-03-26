h_0 = 1000 #altura que se alcanzará en el concurso
h_1 = float(input("Altura (m) actual: "))

t_0 = 0 #primer tiempo
t_1 = float(input("Tiempo (s) actual:"))

v = (h_0-h_1)/(t_1-t_0)

print(f"\nLa velocidad será {v} m/s")