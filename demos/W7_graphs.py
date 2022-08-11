import matplotlib.pyplot as plt
import json

def save(dictio = {}):
    with open("data.json", "w") as f:
        json.dump(dictio, f)

def load():
    with open("data.json") as f:
        data = json.load(f)
    return data

def survey(n = 3):
    c = {}
    for i in range(n):
        resp = input("Who rules in your house? Me, partner, pet, child: ").lower()
        if resp not in {"me", "pet" , "child", "partner"}:
            resp = "pet"
        c[resp] = c.get(resp, 0) + 1
    return c

def run():
    data = {}
    while True:
        print("Menu:\n1-New survey\n2-Load last Survey\n3-Save Results\n4-Visualise\n5-Exit")
        opt = int(input())
        if opt == 1:
            n = int(input("Number of respondents: "))
            data = survey(n)
        elif opt == 2:
            data = load()
        elif opt == 3:
            save(data)
        elif opt == 4:
            print("Choose type:\n1-Point Graph\n2-Bar Chart\n3-Pie Chart")
            opt2 = int(input())
            if opt2 == 1:
                plt.plot(data.keys(), data.values(), "y^")
                plt.show()
            elif opt2 == 2:
                plt.bar(data.keys(), data.values(), color = "#e3ff04")
                plt.show()
            elif opt2 == 3:
                plt.pie(data.values(), labels = data.keys(), autopct = "%.0f")
                plt.show()
        elif opt == 5:
            break


run()