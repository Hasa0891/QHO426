import matplotlib.pyplot as plt
import matplotlib.animation as a
import random

fig, ax = plt.subplots()

def animate(f):
    colours = ["y", "b", "g", "r"]
    color = colours[random.randint(0, 3)]
    ax.cla()
    ax.set_ylim(0,10) 
    ax.set_xlim(0,10)
    ax.plot(f, f, color +"o")

def run():
    fred = a.FuncAnimation(fig, animate, interval = 1000, frames = 10)
    plt.show()

run()