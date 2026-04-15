import matplotlib.pyplot as plt


def jednadzba_pravca(x1, y1, x2, y2):
    if x1 == x2:
        return None, None
    else:
        k = (y2 - y1) / (x2 - x1)
        l = y1 - k * x1
        return k, l


while True:
    try:
        x1 = float(input("Upisi x1: "))
        y1 = float(input("Upisi y1: "))
        x2 = float(input("Upisi x2: "))
        y2 = float(input("Upisi y2: "))
        break
    except:
        print("Pogresan unos, pokusaj opet.")

k, l = jednadzba_pravca(x1, y1, x2, y2)

if x1 == x2:
    x = [x1, x1]
    y = [y1, y2]
else:
    x = [x1, x2]
    y = [k * x1 + l, k * x2 + l]

plt.plot(x, y, label="pravac")
plt.scatter([x1, x2], [y1, y2], color="red", label="tocke")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Pravac kroz dvije tocke")
plt.legend()
plt.grid()

izbor = input("Upisi 1 za prikaz ili 2 za spremanje u PDF: ")

if izbor == "1":
    plt.show()
elif izbor == "2":
    plt.savefig("pravac.pdf")
    print("Graf je spremljen kao pravac.pdf")
else:
    print("Nepoznat izbor")