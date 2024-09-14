"""
This module has classes definition for an arcade machine and a client.

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

class VideogamesMachine():
    """
    This class represents the behavior of an arcade video game machine with its own methods and attributes.
    """

    def __init__(self, material="unknown", games=None):
        """
        Initialize the arcade machine with material, list of games, and price.

        Args:
            material (str): Material of the arcade machine.
            games (list): List of games to be added to the machine. Defaults to an empty list.
        """
        self.material = material
        self.games = games if games is not None else []
        self.price = 0

    def AddGame(self, game: str):
        """
        Add a game to the list of games in the arcade machine.

        This method takes the name of a game as a string and appends it to
        the list of games if the provided input is a string. If an error occurs,
        it logs the error and informs the user.

        Args:
            game (str): The name of the game to add.

        Returns:
            None
        """
        try:
            if isinstance(game, str):
                self.games.append(game)
                result = f"The game {game} has been added to the list of games. :D "

        except Exception as e:
            print(f"ERROR. {e}")
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"{datetime.now()} --- ERROR. {e}.\n")
            result = f"The game {game} has not been added to the list of games. :( "
        print(result)

    def CalculatePrice(self, material_price: float, game_prices: dict):
        """
        Calculate the total price of the arcade machine based on the selected material and games.

        This method calculates the total cost of the arcade machine by summing the cost of the chosen 
        material and the cost of all selected games. It updates the `price` attribute of the 
        `VideogamesMachine` instance to reflect the total cost.

        Args:
            material_price (float): The price of the selected material.
            game_prices (dict): A dictionary where the keys are the names of the games and the values 
            are their respective prices.

        Returns:
            None
        """
        self.price = material_price
        for game in self.games:
            self.price += game_prices.get(game, 0)

class Client():
    """
    This class represents the behavior of a client with its own attributes and methods.
    """

    def __init__(self, name="unknown", address="unknown"):
        """
        Initialize the client with their name and address.

        Args:
            name (str): Name of the client.
            address (str): Address of the client.
        """
        self.name = name
        self.address = address
