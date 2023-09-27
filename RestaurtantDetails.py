

def order_from_restaurant(menu_data, restname, user_name):
        order = []
        total_cost = 0

        print("*" * 50)
        print(f" " * 10, f"Menus for {restname}")
        print("*" * 50)

        # Get the menu for the specified restaurant
        menu = menu_data.get(restname)

        if menu is None:
            print(f"Restaurant '{restname}' not found.")
            return total_cost

        # Initialize a sequence number
        sequence_number = 1

        for item, price in menu.items():
            print(f"{sequence_number}. {item}: ${price:.2f}")
            sequence_number += 1

        while True:
            choice = input("Enter item to add to your order (or 'done' to finish): ")

            if choice == 'done':
                break

            quantity = int(input(f"Enter quantity for {choice}: "))
            order.append((choice, menu[choice], quantity))
            print(f"{quantity} {choice}(s) added to your order.")

        print("*" * 50)
        print(f"Hi {user_name}, Your Order details are:")
        print("*" * 50)

        total_cost = sum(price * quantity for _, price, quantity in order)

        for item, price, quantity in order:
            print(f"{item}: {quantity} x ${price:.2f} = ${price * quantity:.2f}")

        print(f"Total cost: ${total_cost:.2f}")
        print(f"Thank you for ordering, {user_name}!!!!!")
        print("*" * 50)
        return total_cost