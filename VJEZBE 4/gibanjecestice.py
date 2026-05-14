import numpy as np
import matplotlib.pyplot as plt


e = 1.602e-19 # elementarni naboj [C]
m = 9.109e-31 # masa elektrona [kg]


# Električno polje E = (Ex, Ey, Ez)
E = np.array([0.0, 0.0, 1e5])

# Magnetsko polje B = (0, 0, B)
B = np.array([0.0, 0.0, 1.0])


# početni položaj
r = np.array([0.0, 0.0, 0.0])

# početna brzina
v = np.array([2e6, 1e6, 1e6])


# ODABIR ČESTICE

# elektron
q = -e

# za pozitron stavi:
# q 
# VRIJEME

dt = 1e-11 # vremenski korak
N = 5000 # broj koraka
# LISTE ZA SPREMANJE PUTANJE

x_lista = []
y_lista = []
z_lista = []

# GLAVNA PETLJ

for i in range(N):

# Lorentzova sila:
# F = q(E + v x B)

 sila = q * (E + np.cross(v, B))

# akceleracija
a = sila / m

# nova brzina
v = v + a * dt

# novi položaj
r = r + v * dt

# spremanje koordinata
x_lista.append(r[0])
y_lista.append(r[1])
z_lista.append(r[2])

# CRTANJE GRAFA


fig = plt.figure(figsize=(8, 6))

ax = fig.add_subplot(111, projection='3d')

ax.plot(x_lista, y_lista, z_lista)

ax.set_title("Putanja nabijene čestice")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()



