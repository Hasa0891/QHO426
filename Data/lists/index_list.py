def movements():
    return ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]


def run():
    print("Moving...")
    micky_mouse = movements()
    for i in range (0, len(micky_mouse), 2):
        print(f"{micky_mouse[i]} for {micky_mouse[i+1]} steps")

run()