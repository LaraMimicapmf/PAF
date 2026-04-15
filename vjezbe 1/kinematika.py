import matplotlib.pyplot as plt

def jednoliko_gibanje(F, m):
    a = F / m

    t_lista = []
    x_lista = []
    v_lista = []
    a_lista = []

    dt = 0.1
    t = 0
    x = 0
    v = 0

    while t <= 10:
        t_lista.append(t)
        x_lista.append(x)
        v_lista.append(v)
        a_lista.append(a)

        v = v + a * dt
        x = x + v * dt
        t = t + dt

    plt.plot(t_lista, x_lista, label="x-t")
    plt.plot(t_lista, v_lista, label="v-t")
    plt.plot(t_lista, a_lista, label="a-t")

    plt.xlabel("t")
    plt.ylabel("vrijednost")
    plt.title("Jednoliko ubrzano gibanje")
    plt.legend()
    plt.grid()
    plt.show()