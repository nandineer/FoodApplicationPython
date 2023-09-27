from UserDetails import user_details
from RestaurtantDetails import order_from_restaurant
from OrderDetails import payment_for_order
from Order_Confirmation_Mail import order_confirmation_email
import json

print("*" * 50)
print("Welcome to Yummy_Eats: Please login if you are already registered")
print("*" * 50)
user_email = user_details()
user_name,email_addr = user_email

while True:

    # Function to load menu data from a JSON file
    def load_restaurant_data():
        with open('Restaurtants.json', 'r') as rest_file:
            restaurant_data = json.load(rest_file)
        return restaurant_data


    restaurant_data = load_restaurant_data()

    # Function to load menu data from a JSON file
    def load_menu_data():
        with open('MenuDetails.json', 'r') as menu_file:
            menu_data = json.load(menu_file)
        return menu_data


    menu_data = load_menu_data()

    print("*" * 50)
    print(" " * 10, "Restaurants available now")
    print("*" * 50)

    # Initialize a sequence number
    sequence_number = 1

    # Display the JSON data
    for restaurant in restaurant_data:
        print(f"{sequence_number}. Name:",restaurant["name"],",","Cuisine:",restaurant["cuisine"],",","Rating:",restaurant["rating"])
        sequence_number += 1

    rest_choice = input("Select a restaurant to order food (q to quit): ")

    if rest_choice == 'q':
        break

    restaurant_isPresent = False

    for restaurant in restaurant_data:
        if restaurant["name"] == rest_choice:
            restaurant_isPresent = True
            break

    if restaurant_isPresent:
        total_cost = order_from_restaurant(menu_data, rest_choice, user_name)
        payment_for_order(total_cost, user_name)
        order_confirmation_email(email_addr,user_name,total_cost,rest_choice)
    else:
        print("Invalid restaurant")


