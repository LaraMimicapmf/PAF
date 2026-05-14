import math
from particle import Particle   #iz filea particle uzmi klasu particle,model cestie

v0 = 10
<<<<<<< HEAD
kut = math.radians(60)
=======
kut = math.radians(45) #pretvara iz stupnjeva u radijane
>>>>>>> ff3562d9106b45a4544cd03a37c50de477d68c86

cestica = Particle(v0, kut)#napravi jednu cesticu koja ima pocetnu brzinu 10 i kut 45

dt = 0.01  #mali vremenski korak

numericki_domet = cestica.range(dt)  #poziva se metoda range iz parfticle koja resetira cesticu, pomice je korak po korak prati gibanje dok ne padne na tlo i na kraju vraca x ,tj koliko je daleko otisla
analiticki_domet = (v0 ** 2 * math.sin(2 * kut)) / 9.81  #racunamo domet preko poznate formule R=v02 sin(2kut)/g

print("Numericki domet =", numericki_domet)
print("Analiticki domet =", analiticki_domet)

odstupanje = abs(numericki_domet - analiticki_domet)  #apsloutna vrijednos razlike
print("Odstupanje =", odstupanje)

<<<<<<< HEAD
cestica.plot_trajectory(dt)

=======
cestica.plot_trajectory(dt)  #poziva se metoda koja crta putanju cestice
>>>>>>> ff3562d9106b45a4544cd03a37c50de477d68c86
