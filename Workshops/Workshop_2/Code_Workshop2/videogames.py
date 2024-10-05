"""
This module has a class to define a simple videogame.

Author: Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>

This file is part of Workshop2-SM.

Workshop2-SM is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

Workshop2-SM is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with Workshop2-SM. If not, see <https://www.gnu.org/licenses/>. 
"""

class VideoGame:
    """This class represents the behavior of a general videogame."""

    def __init__(self, code: int, name: str, description: str, storytelling_creator: str,
                 graphics_creator: str, category: str, price: float, year: int):
        self.__code = code
        self.__name = name
        self.__description = description
        self.__storytelling_creator = storytelling_creator
        self.__graphics_creator = graphics_creator
        self.__category = category
        self.__price = price
        self.__year = year

    def get_code(self) -> int:
        """This method returns the code of the videogame.
        
        Returns:
            An integer with the code of the videogame.
        """
        return self.__code
    
    def get_category(self) -> str:
        """This method returns the category of the videogame.
        
        Returns:
            A string with the category of the videogame.
        """
        return self.__category
    
    def get_price(self) -> float:
        """This method returns the price of the videogame.
        
        Returns:
            A float with the price of the videogame.
        """
        return self.__price

    def set_description(self, description: str):
        """This method changes the description of the videogame.
        
        Args:
            description (str): New description of the videogame.
        """
        self.__description = description

    def set_description(self, description: str):
        """This method changes the description of the videogame.
        
        Args:
            description (str): New description of the videogame.
        """
        self.__description = description

    def highDefinition(self, high:bool):
        """This method changes the price of the videogame if it is in high definition.
        
        Args:
            description (str): New description of the videogame.
        """
        if high==True:
            self.__price = self.__price+(self.__price*0.1)
        else:
            pass

    def __str__(self) -> str:
        """Returns a string representation of the VideoGame instance."""
        return (
            f"{'=' * 10}\n"
            f"Code: {self.__code}\n"
            f"Name: {self.__name}\n"
            f"Description: {self.__description}\n"
            f"Storytelling Creator: {self.__storytelling_creator}\n"
            f"Graphics Creator: {self.__graphics_creator}\n"
            f"Category: {self.__category}\n"
            f"Price: ${self.__price:.2f}\n"
            f"Year: {self.__year}\n"
            f"{'=' * 10}"
        )
