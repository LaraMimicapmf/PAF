import math


class Projectile:
    def __init__(self, x0, y0, v0, kut, dt):
        self.x0 = x0
        self.y0 = y0
        self.v0 = v0
        self.kut = math.radians(kut) # stupnjevi -> radijani
        self.dt = dt

        self.g = 9.81
        self.k = 0.1 # koeficijent otpora zraka

    def reset(self):
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0 * math.cos(self.kut)
        self.vy = self.v0 * math.sin(self.kut)

        self.x_lista = []
        self.y_lista = []

    def euler(self):
        self.reset()

        while self.y >= 0:
            self.x_lista.append(self.x)
            self.y_lista.append(self.y)

            ax = -self.k * self.vx
            ay = -self.g - self.k * self.vy

            self.x = self.x + self.vx * self.dt
            self.y = self.y + self.vy * self.dt
            self.vx = self.vx + ax * self.dt
            self.vy = self.vy + ay * self.dt

        return self.x_lista, self.y_lista

    def rk4(self):
        self.reset()

        while self.y >= 0:
            self.x_lista.append(self.x)
            self.y_lista.append(self.y)

            dt = self.dt

            k1x = self.vx
            k1y = self.vy
            k1vx = -self.k * self.vx
            k1vy = -self.g - self.k * self.vy

            k2x = self.vx + 0.5 * dt * k1vx
            k2y = self.vy + 0.5 * dt * k1vy
            k2vx = -self.k * (self.vx + 0.5 * dt * k1vx)
            k2vy = -self.g - self.k * (self.vy + 0.5 * dt * k1vy)

            k3x = self.vx + 0.5 * dt * k2vx
            k3y = self.vy + 0.5 * dt * k2vy
            k3vx = -self.k * (self.vx + 0.5 * dt * k2vx)
            k3vy = -self.g - self.k * (self.vy + 0.5 * dt * k2vy)

            k4x = self.vx + dt * k3vx
            k4y = self.vy + dt * k3vy
            k4vx = -self.k * (self.vx + dt * k3vx)
            k4vy = -self.g - self.k * (self.vy + dt * k3vy)

            self.x = self.x + (dt / 6) * (k1x + 2 * k2x + 2 * k3x + k4x)
            self.y = self.y + (dt / 6) * (k1y + 2 * k2y + 2 * k3y + k4y)
            self.vx = self.vx + (dt / 6) * (k1vx + 2 * k2vx + 2 * k3vx + k4vx)
            self.vy = self.vy + (dt / 6) * (k1vy + 2 * k2vy + 2 * k3vy + k4vy)

        return self.x_lista, self.y_lista