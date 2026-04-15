#ZADATAK 3
while True:
    try:
        x1 = float(input("Upisi x1: "))
        y1 = float(input("Upisi y1: "))
        x2 = float(input("Upisi x2: "))
        y2 = float(input("Upisi y2: "))
        break
    except:
        print("Pogresan unos, pokusaj opet.")

if x1 == x2:
    print("Pravac je: x =", x1)
else:
    k = (y2 - y1) / (x2 - x1)
    l = y1 - k * x1
    print("Pravac je: y =", k, "* x +", l)

#ZADATAK 4
def jednadzba_pravca(x1, y1, x2, y2):
    if x1 == x2:
        print("Pravac je: x =", x1)
    else:
        k = (y2 - y1) / (x2 - x1)
        l = y1 - k * x1
        print("Pravac je: y =", k, "* x +", l)


while True:
    try:
        x1 = float(input("Upisi x1: "))
        y1 = float(input("Upisi y1: "))
        x2 = float(input("Upisi x2: "))
        y2 = float(input("Upisi y2: "))
        break
    except:
        print("Pogresan unos, pokusaj opet.")

jednadzba_pravca(x1, y1, x2, y2)