def derivacija_u_tocki(f, x, h=0.0001):
    return (f(x + h) - f(x - h)) / (2 * h)


def derivacija_interval(f, a, b, korak=0.1, h=0.0001):
    lista_x = []
    lista_y = []

    x = a
    while x <= b:
        d = derivacija_u_tocki(f, x, h)
        lista_x.append(x)
        lista_y.append(d)
        x = x + korak

    return lista_x, lista_y


def integral_pravokutnik(f, a, b, n):
    dx = (b - a) / n
    suma = 0
    x = a
    for i in range(n):
        suma = suma + f(x)
        x = x + dx

    return suma * dx


def integral_trapez(f, a, b, n):
    dx = (b - a) / n
    suma = (f(a) + f(b)) / 2
    x = a + dx

    for i in range(1, n):
        suma = suma + f(x)
        x = x + dx
        
    return suma * dx
