def derivacija_u_tocki(f, x, h=0.0001):  #definiramo funkciju , h je mali pomak
    return (f(x + h) - f(x - h)) / (2 * h)   #formula za derivaciju


def derivacija_interval(f, a, b, korak=0.1, h=0.0001):   #imamo funkciju,gornju i donju granicu,razmak medu tockama i korak za samu derivaciju
    lista_x = []
    lista_y = []

    x = a    #krece od pocetka intervala
    while x <= b:  #sve dok ne dode do kraja intervala
        d = derivacija_u_tocki(f, x, h)  #za trenutni x racuna derivaciju pozivom prve funkcije
        lista_x.append(x)   #appenda x u listu
        lista_y.append(d)   #doda derivaciju u listu
        x = x + korak   #pomakni se na sljedecu tocku

    return lista_x, lista_y  #vrati obje liste


def integral_pravokutnik(f, a, b, n):  #odredeni integral kao suma malih pravokutnika ispod grafa
    dx = (b - a) / n   #sirina svakog malog pravokutnika
    suma = 0  #pocetna suma povrsine je 0
    x = a   #krecemo od lijeve strane integracije
    for i in range(n):  #neka petlja ide n puta
        suma = suma + f(x) na sumu dodajemo vrijednost funkcije u toj tocki
        x = x + dx  #pomak na sljedeci pravokutnik

    return suma * dx


def integral_trapez(f, a, b, n):  #trapezna metoda
    dx = (b - a) / n  #sirina svakog trapeza
    suma = (f(a) + f(b)) / 2  #prva i zadnja tocka, tjst rubne tocke trapeza nose pola tezine prema formuli
    x = a + dx  # ne krece se od a nego se ide na prvu unutarnju tocku

    for i in range(1, n):  #idi kroz unutarnje tocke od 1 do n
        suma = suma + f(x)  #dodaje svaku unutarnju visinu
        x = x + dx #pomak dalje
        
    return suma * dx #suma puta pomak dobije se integral
