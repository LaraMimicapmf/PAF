import math
import matplotlib.pyplot as plt
from calculus import derivacija_u_tocki, derivacija_interval, integral_pravokutnik, integral_trapez

def f(x):  #definiramo jednostavno funkciju na kojoj testiraju metode deriviranja i integriranja
    return x**2

    print("Derivacija funkcije x^2 u tocki 2 je:")
    print(derivacija_u_tocki(f, 2))  #pozivamo metodu derivacija_u_tocki s funkcijom f i tockom x=2 

    x_lista, y_lista = derivacija_interval(f, 0, 5, 0.5)  #poziva se metoda na intervalu od 0 do 5 s korakom 0.5

    plt.plot(x_lista, y_lista, marker="o")   #svaka tocka oznacena je s kruzicem
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.title("Numericka derivacija")
    plt.show()

print("Integral pravokutnik:", integral_pravokutnik(f, 0, 2, 100))  #poziva metodu pravokutnika s argumentima f, donja granica integracije,gornja granica int.,broj podjela 
print("Integral trapez:", integral_trapez(f, 0, 2, 100))
