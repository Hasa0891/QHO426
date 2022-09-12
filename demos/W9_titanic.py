import csv
import matplotlib.pyplot as plt

def read_data():
    data = {"survived": [], "sex": [], "fare": [], "age":[]}
    with open("visual/subplots/titanic.csv") as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for row in csv_reader:
            survived = row[1].strip()
            sex = row[14].strip()
            age = row[4].strip()
            fare = row[8].strip()

            if (survived != "" and sex != "" and age != "" and fare != ""):
                data["survived"].append(int(survived))
                data["age"].append(int(round(float(age))))
                if sex == "0":
                    data["sex"].append("male")
                elif sex == "1":
                    data["sex"].append("female")
                data["fare"].append(round(float(fare), 2))             
    return data


def run():
    data = read_data()
    #children 0-17
    #adults 18-64
    #elderly 65->
    ch_survived = 0
    ch_died = 0
    ad_survived = 0
    ad_died = 0
    eld_survived = 0
    eld_died = 0
    for i in range(len(data["age"])):
        if data["age"][i] < 18:
            if data["survived"][i] == 1:
                ch_survived += 1
            else:
                ch_died += 1
        elif data["age"][i] < 65:
            if data["survived"][i] == 1:
                ad_survived += 1
            else:
                ad_died += 1
        else:
            if data["survived"][i] == 1:
                eld_survived += 1
            else:
                eld_died += 1
    fig = plt.figure()
    ax = fig.add_subplot(1, 2, 1)
    ax.bar(["Children", "Adults", "Elderly"], [ch_survived, ad_survived, eld_survived], label = "Survived")
    ax.bar(["Children", "Adults", "Elderly"], [ch_died, ad_died, eld_died], bottom = [ch_survived, ad_survived, eld_survived], label = "Deceased")
    ax.set_title("Age vs Survive")
    ax.legend()

    ax1 = fig.add_subplot(2, 2, 2)
    fares_survived = []
    fares_deceased = []
    for i in range (len(data["survived"])):
        if data["survived"][i] == 1:
            fares_survived.append(data["fare"][i])
        else:
            fares_deceased.append(data["fare"][i])
    ax1.scatter(range(len(fares_survived)), fares_survived, label = "Survived")
    ax1.scatter(range(len(fares_deceased)), fares_deceased, label = "Deceased")
    ax1.legend()
    ax1.set_title("Fares vs Survive")
    plt.show()
                
    #print(f"Survived: {ch_survived}\t Died: {ch_died}")

run()