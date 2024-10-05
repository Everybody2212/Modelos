"""
This module has a class to define the main for a video game machine sales program.

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

import sys
import pickle
import re
from datetime import datetime
from videogames import VideoGame
from machines import Machine
from users import User, Client, Manager, Address
from factoryMachines import PredefinedMachines


# pylint: disable=too-few-public-methods
class Delivery:
    """This class represents the behavior of a delivery in the application."""

    def __init__(self, client_info: Client, address: Address, machine: Machine):
        self.__client_info = client_info
        self.__address = address
        self.__machine = machine

    def __str__(self) -> str:
        return f"{'='*10}\nClient: {self.__client_info}\n\
            Address: {self.__address}\nMachine: {self.__machine}"

#=========================================================================================================
class Main:
    """This class represents the main behavior of the application."""

    MENU_ADMIN = "1.Add Videogame\n2.Remove Videogame\n3.Exit"
    MENU_CLIENT = "1.Buy Machine\n2.Show Registered Machines\n3.Show Videogames\n4.Exit"

    def __init__(self, user: User):
        self.__catalog = []
        self.__temp_machine = None
        self.__user: User = user

    def change_user(self, user: User):
        """This method changes the current user."""
        self.__user = user

    def __validate_videogame_code(self, code: int, machine: Machine) -> bool:
        """This method validates if a videogame code already exists in the catalog.

        In this method, the code of a videogame is received as argument,
        and it is validated if it already exists in the catalog.

        Args:
            code (int): Code of the videogame to be validated.
        """
        for i, vg in enumerate(self.__catalog):
            if vg.get_code() == code:
                return i, vg
        return None

    def add_videogame(self):
        """This method adds a videogame to the catalog of a type of machines."""
        #==============category of the game================
        print("Please select the category of the game to add:\n")
        optionsCategory = "1.Dance Revolution\n2.Classical Arcade\n3.Shooting Machine\n4.Racing Machine\n5.Virtual Reality"
        type_category = int(input(optionsCategory))

        while type_category not in [1, 2, 3, 4, 5]:
            print("Invalid option. Please try again.")
            type_category = int(input(optionsCategory))
        
        if type_category== 1:
            category= "dance"
        elif type_category == 2:
            category= "classical"
        elif type_category == 3:
            category= "shooter"
        elif type_category == 4:
            category= "races"
        elif type_category == 5:
            category= "vr"
        
        code = int(input("Insert the code of the videogame:"))
        while True:
            if self.__validate_videogame_code(code) is not None:
                print("The code already exists, please insert a new one.")
                code = int(input("Insert the code of the videogame:"))
            else:
                break
        while True:
            name = input("Insert the name of the videogame:\n").strip
            if not name:
                print("Invalid input. name cannot be empty.")
            else:
                break
        description = input("Insert the description of the videogame:")
        while True:
            storytelling_creator = input("Please enter the storytelling creator of the videogame:\n").strip()
            if not storytelling_creator:
                print("Invalid input. Storytelling creator cannot be empty.")
            elif any(not char.isalnum() and char not in [' ', '-', "'"] for char in storytelling_creator):
                print("Invalid input. Storytelling creator can only contain letters, numbers, spaces, hyphens, and apostrophes.")
            else:
                break
        while True:
            graphics_creator = input("Please enter the graphics creator of the videogame:\n").strip()
            if not graphics_creator:
                print("Invalid input. Graphics creator cannot be empty.")
            elif any(not char.isalnum() and char not in [' ', '-', "'"] for char in graphics_creator):
                print("Invalid input. Graphics creator can only contain letters, numbers, spaces, hyphens, and apostrophes.")
            else:
                break
        while True:
            price_input = input("Please enter the price of the videogame:\n").strip()
            try:
                price = float(price_input)  # Attempt to convert to float
                if price < 0:
                    print("Invalid input. Price cannot be negative.")
                else:
                    break  # Valid price
            except ValueError:
                print("Invalid input. Please enter a valid number for the price.")
        while True:
            year_input = input("Please enter the year:\n").strip()
            try:
                year = int(year_input)  # Attempt to convert to int
                if year < 1950 or year > 2024: 
                    print("Invalid input. Year must be between 1900 and 2100.")
                else:
                    break  # Valid year
            except ValueError:
                print("Invalid input. Please enter a valid integer for the year.")

        videogame = VideoGame(code, name, description, storytelling_creator,
                graphics_creator, category, price, year)
        self.__catalog.append(videogame)

    def remove_videogame(self):
        """This method removes a videogame from the catalog.

        In this method based on videogame code, if the videogame
        exists it will be removed from current catalog.
        """
        success = False
        code = int(input("Insert the code of the videogame:"))
        response = self.__validate_videogame_code(code)
        if response is not None:
            self.__catalog.pop(response[0])
            success = True

        if success:
            print("Videogame removed successfully.")
        else:
            print(f"Videogame with code {code} is not in the catalog.")


    def add_videogame_to_machine(self):
        """This method adds a videogame to the machine from a specified category."""
        category = input("Please enter the category of the videogame you want to add:\n").strip()  # Ask for the category
        print(f"Looking for videogames in the category: {category}")
        
        # Filter the catalog for videogames in the specified category
        filtered_vg = [vg for vg in self.__catalog if vg.category.lower() == category.lower()]
        
        if not filtered_vg:
            print("No videogames found in this category.")
            return
        
        print("Available videogames in this category:")
        for vg in filtered_vg:  # Display the available videogames in the category
            print(vg)
        
        code = int(input("Insert the code of the videogame you want to add:\n"))  # Ask for the videogame code
        response = self.__validate_videogame_code(code)
        
        if response is not None and response in filtered_vg:  # Check if the videogame is in the filtered list
            print("Do you want it in high definition:\n")
            optionsDefinition = "1.Yes\n2.No"
            type_Definition = int(input(optionsDefinition))

            while type_Definition not in [1, 2]:
                print("Invalid option. Please try again.")
                type_Definition = int(input(optionsDefinition))
            
            if type_Definition== 1:
                response[1].highDefinition(True)
            elif type_Definition == 2:
                response[1].highDefinition(False)

            self.__temp_machine.add_videogame(response[1])
            print("Videogame added successfully.")
        else:
            print("The videogame is not in the catalog or does not belong to the specified category.")

    def show_videogames(self, category=None):
        """This method shows all videogames in the catalog, or only those in the specified category."""
        if category:  # Check if a category has been provided
            print(f"Showing videogames in the category: {category}")
            filtered_vg = [vg for vg in self.__catalog if vg.get_category.lower() == category.lower()]  # Filter by category
            if not filtered_vg:  # If no games found in the category
                print("No videogames found in this category.")
            else:
                for vg in filtered_vg:
                    print(vg)
        else:  # If no category is provided, show all videogames
            print("Showing all videogames in the catalog:")
            for vg in self.__catalog:
                print(vg)

    def __get_delivery_information(self):
        """This method gets the delivery information."""
        print("Choose delivery address:")
        for i, address in enumerate(self.__user.get_addresses()):
            print(f"{i+1}. {address}")
        option = int(input())
        temp_address = self.__user.get_addresses()[option - 1]
        delivery = Delivery(self.__user, temp_address, self.__temp_machine)

        file_name = f"delivery_{datetime.now().strftime('%Y-%m-%d_%H%M%S')}_\
            {self.__user.get_id()}.pkl"
        with open(file_name, "wb") as file:
            pickle.dump(delivery, file)

        print("Delivery will be sent to:", self.__user.get_addresses()[option - 1])

    def buy_machine(self):
        """This method buys the machine."""

        #==============predefined machine================
        print("Please select the machine to buy:\n")
        optionsCategory = "1.Dance Revolution\n2.Classical Arcade\n3.Shooting Machine\n4.Racing Machine\n5.Virtual Reality"
        type_category = int(input(optionsCategory))

        while type_category not in [1, 2, 3, 4, 5]:
            print("Invalid option. Please try again.")
            type_category = int(input(optionsCategory))
        
        if type_category== 1:
            category= "dance"
        elif type_category == 2:
            category= "classical"
        elif type_category == 3:
            category= "shooter"
        elif type_category == 4:
            category= "races"
        elif type_category == 5:
            category= "vr"

        #==============choose material=================
        print("Please select the material:\n")
        optionsMaterial = "1.Wood\n2.Aluminium\n3.Carbon Fiber"
        type_material = int(input(optionsMaterial))

        while type_material not in [1, 2, 3]:
            print("Invalid option. Please try again.")
            type_material = int(input(optionsMaterial))
        
        if type_material== 1:
            material= "wood"
        elif type_material == 2:
            material= "aluminium"
        elif type_material == 3:
            material= "carbon_fiber"
        
        #=====================color=========================
        while True:
            print("Please write the color:\n")
            color = input().strip() 
            
            if not color: 
                print("Invalid input. Color cannot be empty.")
            elif any(not char.isalpha() and char not in [' ', '-', "'"] for char in color): 
                print("Invalid input. Color can only contain letters, spaces, hyphens, and apostrophes.")
            else:
                break

        machines = PredefinedMachines()
        self.__temp_machine=machines.create_machine(category,color,material)

        #===========================Videogames and Price=======================
        optionAddVG=-1
        print("Please select the option you want:\n")
        MenuAddVG = "1.Add videogame to the machine\n2.Exit"
        optionAddVG = int(input(MenuAddVG))
        while optionAddVG!=2:
            self.add_videogame_to_machine
            print("Please select the option you want:\n")
            optionAddVG = int(input(MenuAddVG))

        price_videogames = sum(vg.get_price() for vg in self.__temp_machine.get_videogames())
        total_price = self.__temp_machine.get_price() + price_videogames
        
        print("\nPurchased Machine Details:")
        print(self.__temp_machine.__str__())
        print(f"\nTotal price: {total_price}")

        # Save the machine details to a file
        with open("registered_machines.txt", "a") as file:
            file.write(f"{category.capitalize()}, {material.capitalize()}, {color.capitalize()}, ${total_price:.2f}\n")
        
        if isinstance(self.__user, Client):
            if self.__temp_machine is not None:
                self.__get_delivery_information()
                self.__temp_machine = None
            else:
                print("You must choose a material first and add videogames.")
        else:
            print("You do not have permission to buy a machine.")
        
    def show_registered_machines(self):
        """This method shows all registered machines with search capabilities."""
        try:
            with open("registered_machines.txt", "r") as file:
                lines = file.readlines()
                
                if not lines:
                    print("No registered machines found.")
                    return
                
                # Parse machines into a structured list of dictionaries
                machines = []
                for line in lines:
                    parts = line.strip().split(", ")
                    if len(parts) == 4:
                        category, material, color, price = parts
                        machines.append({
                            "category": category,
                            "material": material,
                            "color": color,
                            "price": float(price.replace("$", "").replace(",", ""))  # Convert price to float
                        })

                # Ask user for search criteria
                print("Would you like to search for specific machines? (yes/no)")
                search_response = input().strip().lower()
                if search_response == "yes":
                    # Gather search criteria
                    price_range = input("Enter price range (min,max) or leave blank: ").strip()
                    material_type = input("Enter material type or leave blank: ").strip()
                    
                    # Filter machines based on criteria
                    filtered_machines = machines
                    
                    if price_range:
                        min_price, max_price = map(float, price_range.split(","))
                        filtered_machines = [m for m in filtered_machines if min_price <= m['price'] <= max_price]

                    if material_type:
                        filtered_machines = [m for m in filtered_machines if m['material'].lower() == material_type.lower()]


                    # Display filtered results
                    if filtered_machines:
                        print("Filtered Registered Machines:")
                        for machine in filtered_machines:
                            print(f"{machine['category']}, {machine['material']}, {machine['color']}, ${machine['price']:.2f}")
                    else:
                        print("No machines match your search criteria.")
                else:
                    print("Displaying all registered machines:")
                    for machine in machines:
                        print(f"{machine['category']}, {machine['material']}, {machine['color']}, ${machine['price']:.2f}")

        except FileNotFoundError:
            print("The file 'registered_machines.txt' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")


    def show_menu(self):
        """This method shows the menu according to the user type."""
        if isinstance(self.__user, Manager):
            print(Main.MENU_ADMIN)
        elif isinstance(self.__user, Client):
            print(Main.MENU_CLIENT)

    def __handle_admin(self, option: int):
        exit_ = False
        if option == 1:  # add videogame
            self.add_videogame()
        elif option == 2:  # remove videogame
            self.remove_videogame()
        elif option == 3:  # exit
            print("Manager view is closing!")
            exit_ = True

        return exit_

    def __handle_client(self, option: int) -> bool:
        exit_ = False
        if option == 1:  # Buy machine
            self.buy_machine()
        elif option == 2:  # show registered machines
            self.show_registered_machines()
        elif option == 3:  # show videogames
            self.show_videogames()
        elif option == 4:  # exit
            print("Client view is closing!")
            exit_ = True

        return exit_

    def handle_option(self, option: int) -> bool:
        """This method handles the option selected by the user.

        Args:
            option (int): Option selected by the user.
        """
        if isinstance(self.__user, Manager):
            exit_ = self.__handle_admin(option)
        elif isinstance(self.__user, Client):
            exit_ = self.__handle_client(option)
        return exit_


# ======================= main execution ======================= #


def get_user() -> User:
    """This function gets the user type."""
    options = "1.Manager\n2.Client\n3.Exit"
    type_user = int(input(options))

    while type_user not in [1, 2, 3]:
        print("Invalid option. Please try again.")
        type_user = int(input(options))

    user = None
    if type_user == 1:
        while True:
            print("Please insert your ID:\n")
            try:
                idAdmin = int(input()) 
                if idAdmin < 0:
                    print("Invalid ID. Please enter a positive integer.")
                else:
                    print(f"Your ID is: {idAdmin}")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer ID.")
        
        while True:
            print("Please insert your name:\n")
            nameAdmin = input().strip() 
            if not nameAdmin:  
                print("Invalid input. Name cannot be empty.")
            elif any(char.isdigit() for char in nameAdmin):  
                print("Invalid input. Name cannot contain numbers.")
            elif any(not char.isalpha() and char not in [' ', '-', "'"] for char in nameAdmin):  
                print("Invalid input. Name can only contain letters, spaces, hyphens, and apostrophes.")
            else:
                print(f"Your name is: {nameAdmin}")
                break

        while True:
            print("Please insert your email:\n")
            emailAdmin = input().strip()
            if not emailAdmin: 
                print("Invalid input. Email cannot be empty.")
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", emailAdmin): 
                print("Invalid input. Please enter a valid email address.")
            else:
                print(f"Your email is: {emailAdmin}")
                break

        user = Manager(idAdmin, nameAdmin, emailAdmin)

    elif type_user == 2:
        while True:
            street = input("Please insert your street:\n").strip()
            if not street:
                print("Invalid input. Street cannot be empty.")
            elif any(not char.isalnum() and char not in [' ', '-', '.'] for char in street):
                print("Invalid input. Street can only contain letters, numbers, spaces, hyphens, and periods.")
            else:
                break 

        while True:
            zip_code_input = input("Please insert your zip code:\n").strip()
            try:
                zip_code = int(zip_code_input) 
                if zip_code < 0:
                    print("Invalid input. Zip code cannot be negative.")
                else:
                    break 
            except ValueError:
                print("Invalid input. Please enter a valid integer for the zip code.")

        while True:
            city = input("Please insert your city:\n").strip()
            if not city:
                print("Invalid input. City cannot be empty.")
            elif any(not char.isalpha() and char not in [' ', '-', "'"] for char in city):
                print("Invalid input. City can only contain letters, spaces, hyphens, and apostrophes.")
            else:
                break 

        while True:
            country = input("Please insert your country:\n").strip()
            if not country:
                print("Invalid input. Country cannot be empty.")
            elif any(not char.isalpha() and char not in [' ', '-', "'"] for char in country):
                print("Invalid input. Country can only contain letters, spaces, hyphens, and apostrophes.")
            else:
                break
        address = Address(street, zip_code, city, country)

        while True:
            print("Please insert your ID:\n")
            try:
                idClient = int(input()) 
                if idClient < 0:
                    print("Invalid ID. Please enter a positive integer.")
                else:
                    print(f"Your ID is: {idClient}")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer ID.")
        
        while True:
            print("Please insert your name:\n")
            nameClient = input().strip() 
            if not nameClient:  
                print("Invalid input. Name cannot be empty.")
            elif any(char.isdigit() for char in nameClient):  
                print("Invalid input. Name cannot contain numbers.")
            elif any(not char.isalpha() and char not in [' ', '-', "'"] for char in nameClient):  
                print("Invalid input. Name can only contain letters, spaces, hyphens, and apostrophes.")
            else:
                print(f"Your name is: {nameClient}")
                break

        while True:
            print("Please insert your email:\n")
            emailClient = input().strip()
            if not emailClient: 
                print("Invalid input. Email cannot be empty.")
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", emailClient): 
                print("Invalid input. Please enter a valid email address.")
            else:
                print(f"Your email is: {emailClient}")
                break

        while True:
            phoneClient = input("Please insert your phone number:\n").strip()
            
            if not phoneClient: 
                print("Invalid input. Phone number cannot be empty.")
            elif not re.match(r'^\+?\d[\d -]{6,14}\d$', phoneClient): 
                print("Invalid input. Please enter a valid phone number (e.g., +1234567890, 123-456-7890).")
            else:
                break  

        user = Client(
            idClient, nameClient, emailClient, phoneClient, address
        )
    elif type_user == 3:
        print("Thanks for using the application. Goodbye!")
        sys.exit()

    return user


def run():
    """This function runs the application."""
    user = get_user()
    main = Main(user)

    while True:
        while True:
            main.show_menu()
            option = int(input("Enter the option:"))
            if main.handle_option(option):
                break

        user = get_user()
        main.change_user(user)


if __name__ == "__main__":
    run()
