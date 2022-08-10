def shop():
    items = {"ipod": 500, "mouse": 9.99, "potatoes": 1.99, "gold": 9999.99, "bread": 2.19, "python tuition": 0.99, "carrot": 0.29}
    return items

def view_all(products = {}):
    for i, j in products.items():
        print(f"{i}-------------£{j:.2f}")

def basket():
    b = []
    while True:
        item = input("Enter next item or \"stop\" to stop: ")
        if item.upper() == "STOP":
            break
        q = int(input(f"Enter the quantity of {item}: "))
        for i in range(q):
            b.append(item.lower())
    return b

def till(basket = []):
    all_items = shop()
    total = 0.0
    for product in basket:
        if product in all_items:
            total += all_items[product]
        else:
            print(f"Sorry mate, the {product} is not available. Go to Lidl")
    return total

def run():
    print("Welcome to Pete's shop. Please look around. Items available: ")
    view_all(shop())
    b = basket()
    while True:
        print("Are you ready to pay? [Y/N]")
        response = input().upper()
        if response[0] == "Y":
            to_pay = till(b)
            print(f"Pay £{to_pay:.2f} or I will come after you")
            break
        else:
            b2 = basket()
            b.extend(b2)

run()