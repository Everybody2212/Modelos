"""
This module has a class to define users in the context of 
the application.

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


from abc import ABC, abstractmethod


# ========== Address Class ========== #
class Address:  # abstract data type
    """This class represents the behavior of an address in the application."""

    def __init__(
        self, street: str, zip_code: int, city: str, country: str):
        self.__street = street
        self.__zip_code = zip_code
        self.__city = city
        self.__country = country

    def __str__(self) -> str:
        return f"{'='*10}\nStreet: {self.__street}\nZip Code: {self.__zip_code}\n\
            City: {self.__city}\nCountry: {self.__country}"


# ========== User AbstractClass ========== #
class User(ABC):
    """This class represents the behavior of a general
    user in the application, it acts as an abstract class."""

    def __init__(self, id_: int, name: str, email: str):
        self._id = id_
        self._name = name
        self._email = email
        self._grants = None

    def get_id(self) -> int:
        """This method returns the id of the user.

        Returns:
            An integer with the id of the user.
        """
        return self._id



# ========== Client Class ========== #
class Client(User):
    """This class represents the behavior of a general client in the application."""

    def __init__(self, id_: int, name: str, email: str, phone: str, address: Address):
        super().__init__(id_, name, email)
        self.__phones = [phone]
        self.__addresses = [address]

    def add_phone(self, phone: str):
        """This method adds an additional phone number to the client.

        In this method a phone in string format is taken and added at the
        end of the list of user's phones.

        Args:
            phone (str): Phone number to be added.
        """
        self.__phones.append(phone)

    def add_address(
        self, street: str, zip_code: int, city: str, country: str = "Colombia"
    ):
        """This method adds an additional address to the client.

        In this method an address is created and added at the end of the
        list of user's addresses.

        Args:
            street (str): Street of the address.
            zip_code (int): Zip code of the address.
            city (str): City of the address.
            country (str): Country of the address.
        """
        address_temp = Address(street, zip_code, city, country)
        self.__addresses.append(address_temp)

    def get_addresses(self) -> list:
        """This method returns the list of addresses of the client.

        Returns:
            A list with the addresses of the client.
        """
        return self.__addresses

    def __str__(self):
        return f"Name: {self._name}\nEmail: {self._email}\nPhones:{' --- '.join(self.__phones)}"

# ========== Manager Class ========== #
class Manager(User):
    """This class represents the behavior of a general manager in the application."""

    def __init__(self, id_: int, name: str, email: str):
        super().__init__(id_, name, email)
