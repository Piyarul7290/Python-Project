
menu = {"pizza": 3.00,
        "hot dog": 4.50,
        "soda": 1.24,
        "fries": 3.89,
        "ice cream": 4.99,
        "salad":5.99}

cart = []
total = 0

print("-----------MENU-----------")
for key, value in menu.items():
        print(f"{key:10}: ${value:.2f}")
print("--------------------------")


while True:
        food = input("Select an item item (q to quit): ").lower()
        if food == 'q':
                break
        elif menu.get(food) is not None:
                cart.append(food)

print("-----------CART-----------") 
for food in cart:
        total += menu.get(food)
        print(food, end=" ")

print()
print(f"Total: ${total:.2f}")
