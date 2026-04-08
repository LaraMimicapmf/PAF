import math
import matplotlib.pyplot as plt
from particle import Particle

v0 = 10
kut = math.radians(60)

tocan_domet = (v0 ** 2 * math.sin(2 * kut)) / 9.81

lista_dt = [0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005]
lista_pogreski = []

for dt in lista_dt:
    cestica = Particle(v0, kut)
    numericki_domet = cestica.range(dt)

    relativna_pogreska = abs(numericki_domet - tocan_domet) / abs(tocan_domet)
    lista_pogreski.append(relativna_pogreska)

    print("dt =", dt, " pogreska =", relativna_pogreska)

plt.plot(lista_dt, lista_pogreski, marker="o")
plt.xlabel("dt")
plt.ylabel("Relativna pogreska")
plt.title("Ovisnost relativne pogreske o dt")
plt.show()