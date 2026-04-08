import math
from particle import Particle

v0 = 10
kut = math.radians(45)

cestica = Particle(v0, kut)

dt = 0.01

numericki_domet = cestica.range(dt)
analiticki_domet = (v0 ** 2 * math.sin(2 * kut)) / 9.81

print("Numericki domet =", numericki_domet)
print("Analiticki domet =", analiticki_domet)

odstupanje = abs(numericki_domet - analiticki_domet)
print("Odstupanje =", odstupanje)

cestica.plot_trajectory(dt)