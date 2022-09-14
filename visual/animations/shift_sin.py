import matplotlib.pyplot as plt
import matplotlib.animation as a
import numpy as np

fig, ax = plt.subplots()

def animate(f):
    ax.cla()
    ax.set_xlim(0,720)
    ax.set_ylim(-1,1)
    x_degree = np.arange(0, 720)
    x_rad = x_degree * np.pi / 180
    y = np.sin(x_rad - f/20)
    ax.plot(x_degree, y, "bo")

def run():
    jack = a.FuncAnimation(fig, animate, interval = 100, frames = 720)
    plt.show()
