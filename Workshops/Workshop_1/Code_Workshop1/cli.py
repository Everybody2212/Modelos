"""
This module has simple CLI for a video game arcade machine purchasing program manipulation.

Author: Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>

This file is part of Workshop1-ArcMach.

Workshop1-ArcMach is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

Workshop1-ArcMach is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with Workshop1-ArcMach. If not, see <https://www.gnu.org/licenses/>. 
"""
from datetime import datetime
from machine_classes import VideogamesMachine
from machine_classes import Client

def record_purchase(client_name, price):
    """
    Record a purchase with the current date, client name, and price.

    Args:
        client_name (str): The name of the client.
        price (float): The total price of the purchase.

    Returns:
        None
    """
    with open("purchase_history.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} --- Client: {client_name}, Total Price: ${price}\n")


def show_purchase_history():
    """
    Display the purchase history from the file.

    Returns:
        None
    """
    try:
        with open("purchase_history.txt", "r", encoding="utf-8") as f:
            history = f.readlines()
            if history:
                print("\nPurchase History:")
                for line in history:
                    print(line.strip())
            else:
                print("No purchase history found.")
    except FileNotFoundError:
        print("No purchase history file found.")

if __name__ == "__main__":
    print("Welcome, here you can buy the arcade video game machine of your choice")

    MENU = """
    1. Buy
    2. Purchase History
    3. Exit\n
    """

    material_prices = {
        "wood": 150,
        "aluminum": 250,
        "carbon fiber": 350
    }
    game_prices = {
        "Space Invaders": 50,
        "Pac-Man": 60,
        "Donkey Kong": 55,
        "Street Fighter": 70,
        "Galaga": 65,
        "Tetris": 45,
        "Frogger": 50,
        "Asteroids": 55,
        "Centipede": 60
    }

    option = int(input(MENU))
    while option != 3:
        if option == 1:
            client = Client()

            print("Please enter your details below:\n")

            client.name = input("Name: ")
            client.address = input("Address: ")

            while True:
                MaterialMenu = """\nPlease choose the material for the arcade machine:
                1. Wood ($150)
                2. Aluminum ($250)
                3. Carbon Fiber ($350)\n
                """

                material_option = int(input(MaterialMenu))
                materials = {
                    1: "wood",
                    2: "aluminum",
                    3: "carbon fiber"
                }

                if material_option in materials:
                    selected_material = materials[material_option]
                    arcade_machine = VideogamesMachine(material=selected_material)
                    print(f"You have selected a {selected_material} arcade machine.")
                    material_cost = material_prices[selected_material]
                    break
                else:
                    print("Invalid material option selected. Please choose again.")

            GamesCatalog = """\nPlease choose the games that you want in your machine.

            Game Catalog:
            1. Space Invaders ($50)
            2. Pac-Man ($60)
            3. Donkey Kong ($55)
            4. Street Fighter ($70)
            5. Galaga ($65)
            6. Tetris ($45)
            7. Frogger ($50)
            8. Asteroids ($55)
            9. Centipede ($60)
            10. Finish Game Selection\n
            """

            selected_game = 0
            selected_games = set()  # Set to track selected games
            while selected_game != 10:
                selected_game = int(input(GamesCatalog))
                games = {
                    1: "Space Invaders",
                    2: "Pac-Man",
                    3: "Donkey Kong",
                    4: "Street Fighter",
                    5: "Galaga",
                    6: "Tetris",
                    7: "Frogger",
                    8: "Asteroids",
                    9: "Centipede"
                }

                if selected_game in games:
                    game_name = games[selected_game]
                    if game_name not in selected_games:
                        arcade_machine.AddGame(game_name)
                        selected_games.add(game_name)
                    else:
                        print(f"The game {game_name} is already selected. Please choose another.")
                elif selected_game != 10:
                    print("Invalid game option. Please choose again.")

            arcade_machine.CalculatePrice(material_cost, game_prices)

            while True:
                print("\nPurchase Summary:")
                print(f"Client Name: {client.name}")
                print(f"Client Address: {client.address}")
                print(f"Arcade Machine Material: {selected_material}")
                print(f"Material Cost: ${material_cost}")
                print("Games in the Arcade Machine:")
                if arcade_machine.games:
                    for game in arcade_machine.games:
                        print(f"- {game} (${game_prices[game]})")
                else:
                    print("No games selected.")
                print(f"Total Cost of Games: ${sum(game_prices[game] for game in arcade_machine.games)}")
                print(f"Total Cost: ${arcade_machine.price}")

                continue_option = input("\nWould you like to buy or cancel? (Type 'buy' to purchase or 'cancel' to return to the menu): ").strip().lower()
                if continue_option == 'buy':
                    record_purchase(client.name, arcade_machine.price)
                    print("Purchase recorded. Returning to main menu.")
                    break
                elif continue_option == 'cancel':
                    print("Purchase canceled. Returning to main menu.")
                    break
                else:
                    print("Invalid option. Please type 'buy' to purchase or 'cancel' to return to the menu.")

        elif option == 2:
            show_purchase_history()
        else:
            print("Please, choose a valid option.")

        if option != 3:
            option = int(input(MENU))
