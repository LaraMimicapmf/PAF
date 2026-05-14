import math
import matplotlib.pyplot as plt
from particle import Particle   #uvozim klasu particle iz filea particle

v0 = 10
kut = math.radians(60)

tocan_domet = (v0 ** 2 * math.sin(2 * kut)) / 9.81  #racunamo tocan analiticki domet

lista_dt = [0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005]  #radimo listu razlicith vremenskih koraka, to su vrijednosti za delta t,ako je dt velik simulacija je manje precizna
lista_pogreski = []  #tu kasnije stavljamo sve izracunate pogreske

for dt in lista_dt:  #profi kroz sve vrijednosti iz liste 
    cestica = Particle(v0, kut)# za svaki dt to jest vremenski korajk stvaramo novu cesticu
    numericki_domet = cestica.range(dt)  #koristimo range metodu kako bi racunali numericki domet za trenutni vremenski korak, tjst cestica krece od pcetka,pomice se korak po korak,korak traje dt, kad padne na tlo, metoda vraca x

    relativna_pogreska = abs(numericki_domet - tocan_domet) / abs(tocan_domet)  #abslutna razlika 2 dometa,gledamo udio greske u odnosu na tocnu vrijednost
    lista_pogreski.append(relativna_pogreska)  #spremamo izracunatu relativnu pogresku u listu

    print("dt =", dt, " pogreska =", relativna_pogreska)

plt.plot(lista_dt, lista_pogreski, marker="o")#x os lista, y os lista pogreski i svaka tocka ce biti iznacena s kruzicem
plt.xlabel("dt")
plt.ylabel("Relativna pogreska")
plt.title("Ovisnost relativne pogreske o dt")
plt.show()
