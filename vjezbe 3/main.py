import matplotlib.pyplot as plt
from projectile import Projectile

p = Projectile(0, 0, 20, 45, 0.5)

x1, y1 = p.euler()
x2, y2 = p.rk4()

plt.plot(x1, y1, label="Euler")
plt.plot(x2, y2, label="RK4")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Projectile motion with air resistance")
plt.legend()
plt.grid()
plt.show()