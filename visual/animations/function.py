import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(frame):
    print(frame)

def run():
    fig, ax = plt.subplots()
    bob = animation.FuncAnimation(fig, animate, interval = 1000, frames = 10, repeat = False)
    plt.show()


run()