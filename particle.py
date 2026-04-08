import math
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, kut, x0=0, y0=0):
        self.v0 = v0
        self.kut = kut
        self.x0 = x0
        self.y0 = y0
        self.g = 9.81
        self.reset()

    def reset(self):
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0 * math.cos(self.kut)
        self.vy = self.v0 * math.sin(self.kut)

    def __move(self, dt):
        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy * dt
        self.vy = self.vy - self.g * dt

    def range(self, dt):
        self.reset()
        while self.y >= 0:
            self.__move(dt)
        return self.x

    def plot_trajectory(self, dt):
        self.reset()
        lista_x = []
        lista_y = []

        while self.y >= 0:
            lista_x.append(self.x)
            lista_y.append(self.y)
            self.__move(dt)

        plt.plot(lista_x, lista_y)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Putanja cestice")
        plt.show()