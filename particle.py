import math
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, kut, x0=0, y0=0):      #pamti pocetne uvjete 
        self.v0 = v0
        self.kut = kut
        self.x0 = x0
        self.y0 = y0
        self.g = 9.81
        self.reset()  #konkretno pocetno stanje

    def reset(self):  #vraca polozaj na pocetne koordinate
        self.x = self.x0  #trenutni x je xo
        self.y = self.y0
        self.vx = self.v0 * math.cos(self.kut)  #horizontalna komponentqa brzine,ostaje stalna jer nema otporqa zraka
        self.vy = self.v0 * math.sin(self.kut)  #vertikalna komponenta brzine,mijenja se zbog gravitacije

    def __move(self, dt):  #ova metoda pomice cesticu za mali vremenski korak dt,_move znaci da je privatna metoda
        self.x = self.x + self.vx * dt  #novi polozaj=stari polozaj +brzina*vrijeme
        self.y = self.y + self.vy * dt  #polozaj se mijenja ovisno o vertikalnoj brzini
        self.vy = self.vy - self.g * dt #ubrzanje,gravitacija,minus jer vuce prema dolje

    def range(self, dt):#racuna domet, koliko daleko padne cestica
        self.reset()  #vrati cesticu na pocetak
        while self.y >= 0:#ponavljaj petlju  dok je cestica iznad tla,ako padne ispod stop
            self.__move(dt)  #ovo poziva privatnu metodu koja napravi jedan mali korak gibanja 
        return self.x  #na kraju vraca koliko je daleko otisla po x osi

    def plot_trajectory(self, dt):  #sprema putanju cestice
        self.reset()  #vrati cesticu na pocetak
        lista_x = []  #sve x pozicije
        lista_y = []   #sve y pozicije

        while self.y >= 0:  #opet petlja radi dok je cestica iznad tla
            lista_x.append(self.x) #u listu dodajes trenutni x,append doda na kraj liste
            lista_y.append(self.y)  #spremam u listu trenutnu visinu cestice
            self.__move(dt) #pomaknemo cesticu opet za mali korak, onda ce u sljedećem prolazu petlje imati novu poziciju

        plt.plot(lista_x, lista_y)  #koordinate
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Putanja cestice")
        plt.show()
