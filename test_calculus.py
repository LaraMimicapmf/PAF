import math
import matplotlib.pyplot as plt
from calculus import derivacija_u_tocki, derivacija_interval, integral_pravokutnik, integral_trapez

def f(x):
    return x**2

    print("Derivacija funkcije x^2 u tocki 2 je:")
    print(derivacija_u_tocki(f, 2))

    x_lista, y_lista = derivacija_interval(f, 0, 5, 0.5)

    plt.plot(x_lista, y_lista, marker="o")
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.title("Numericka derivacija")
    plt.show()

print("Integral pravokutnik:", integral_pravokutnik(f, 0, 2, 100))
print("Integral trapez:", integral_trapez(f, 0, 2, 100))