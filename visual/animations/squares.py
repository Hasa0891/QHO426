import matplotlib.pyplot as plt
import matplotlib.animation as a

boxes = []
fig, ax = plt.subplots()
colour = ["r-", "b--", "y.-", "p--", "g-"]

def init():
    boxes.append({"x": [5, 5, 6, 6, 5] , "y": [4, 5, 5, 4, 4] })
    boxes.append({"x": [7, 7, 4, 4, 7] , "y": [6, 3, 3, 6, 6]})
    boxes.append({"x": [0, 0, 10, 10, 0] , "y": [0, 10, 10, 0, 0]})

def animate(f):
    if f % 3 == 0:
        ax.cla()
    ax.set_xlim(-2, 12)
    ax.set_ylim(-2, 12)
    ax.plot(boxes[f % 3]["x"], boxes[f % 3]["y"], colour[f % 5])

def run():
    harry = a.FuncAnimation(fig, animate, frames = 99, interval = 1000, init_func = init)
    plt.show()

run()