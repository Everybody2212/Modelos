"""
This module has a class to define the machines in the context of 
the application.

Author: Anderson David Arenas Gutierrez <adarenasg@udistrital.edu.co>

This file is part of Workshop2-SM.

Workshop-SM is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

Workshop-SM is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with Workshop-SM. If not, see <https://www.gnu.org/licenses/>. 
"""

from abc import ABC, abstractmethod
from videogames import VideoGame

#================================ Abstract class =============================================

class Machine(ABC):
    """This class represents the behavior of a general
    machine in the application, it acts as an abstract class."""

    def __init__(self, material: str, dimensions: list, weight: float, power_consumption: float,
                  memory: int, processors: str, base_price: float):
        self.material = material
        self.__dimensions = dimensions
        self.__weight = weight
        self.__power_consumption = power_consumption
        self.__memory = memory
        self.__processors = processors
        self.__base_price = base_price
        self.__price = base_price
        self.__videogames = []

    def get_videogames(self):
        """This method returns the videogames of the machine.
        
        Returns:
            A list with the videogames of the machine.
        """
        return self.__videogames
    
    def get_price(self):
        """This method returns the price of the machine.
        
        Returns:
            A float with the price of the machine.
        """
        return self.__price

    @abstractmethod
    def add_videogame(self, videogame: VideoGame):
        """This method adds a videogame to the current machine.

        In this method a videogame is received as argument,
        following a VideoGame abstract data type, and it is 
        add to internal games list.

        Args:
            videogame (VideoGame): videogame to be added
        """
        self.__videogames.append(videogame)

    def adjustmentsByMaterial(self):
        if self.material=="wood":
            self.__weight= self.__weight+(self.__weight*0.1)
            self.__price= self.__price-(self.__price*0.05)
            self.__power_consumption= self.__power_consumption+(self.__power_consumption*0.15)
        if self.material=="aluminium":
            self.__weight= self.__weight-(self.__weight*0.05)
            self.__price= self.__price+(self.__price*0.1)
        if self.material=="carbon_fiber":
            self.__weight= self.__weight-(self.__weight*0.15)
            self.__price= self.__price+(self.__price*0.2)
            self.__power_consumption= self.__power_consumption-(self.__power_consumption*0.1)

    def remove_videogame(self, code: int):
        """This method removes a videogame from the machine.

        In this method based on videogame code, if the videogame 
        exists it will be removed from current machine.

        Args:
            code (int): Code of the videogame to be removed.
        """
        index = -1 # logic mark
        for i, vg in enumerate(self.__videogames):
            if vg.get_code() == code:
                index = i
                break

        if index != -1: # videogame is in machine
            self.__videogames.pop(index)
        else:
            print(f"VideoGame with code {code} it not in the machine.")

    def show_videogames(self):
        """This method show all videogames in the current machine.

        In this method the list of videogames is printed following
        a format of code and name.
        """
        if len(self.__videogames) > 0:
            print("Code\tName")
            for vg in self.__videogames:
                print(vg)
        else:
            print("No videogames have been added.")

    def __str__(self) -> str:
        temp_videogames = ""
        for vg in self.__videogames:
            temp_videogames += str(vg) + "\n"
        
        return (
            f"{'*' * 15}\n"
            f"Material: {self.material}\n"
            f"Dimensions: {self.__dimensions} cm\n"
            f"Weight: {self.__weight} kg\n"
            f"Power Consumption: {self.__power_consumption} W\n"
            f"Memory: {self.__memory} MB\n"
            f"Processors: {self.__processors}\n"
            f"Base Price: ${self.__base_price:.2f}\n"
            f"Videogames:\n{temp_videogames if temp_videogames else 'No videogames installed'}"
        )

#================================== Concrete class =========================================
class DanceRevolution(Machine):
    """This class represents the behavior of a dance revolution
    machine in the application."""

    def __init__(self, material: str, dimensions: list, weight: float, power_consumption: float,
                  memory: int, processors: str, base_price: float, color: str, difficulties: list, arrow_cardinalities: list, 
                  controls_price: float):
        
        super.__init__(material,dimensions,weight,power_consumption,memory,processors,base_price)
        self.color = color
        self.__price = base_price + controls_price
        self.__difficulties = difficulties
        self.__arrow_cardinalities = arrow_cardinalities
        self.__controls_price = controls_price

    def add_videogame(self, videogame: VideoGame):
        """This method adds a videogame to the current Dance Revolution machine.

        In this method a videogame is received as argument,
        following a VideoGame abstract data type, and it is 
        add to internal games list.

        Args:
            videogame (VideoGame): videogame to be added
        """
        if videogame.get_category=="dance":
            self.__videogames.append(videogame)
        else:
            print(f"The videogame can not be added because its category is not compatible")

    def __str__(self) -> str:
        difficulties_str = ', '.join(self.__difficulties)
        arrow_cardinalities_str = ', '.join(self.__arrow_cardinalities)
        temp_videogames = ""
        for vg in self.__videogames:
            temp_videogames += str(vg) + "\n"
        
        return (
            f"{'*' * 15}\n"
            f"Material: {self.material}\n"
            f"Color: {self.color}\n"
            f"Dimensions: {self.__dimensions} cm\n"
            f"Weight: {self.__weight} kg\n"
            f"Power Consumption: {self.__power_consumption} W\n"
            f"Memory: {self.__memory} MB\n"
            f"Processors: {self.__processors}\n"
            f"Difficulties: {difficulties_str}\n"
            f"Arrow Cardinalities: {arrow_cardinalities_str}\n"
            f"Controls Price: ${self.__controls_price:.2f}\n"
            f"Base Price: ${self.__base_price:.2f}\n"
            f"Videogames:\n{temp_videogames if temp_videogames else 'No videogames installed'}"
            )
        

    
class ClassicalArcade(Machine):
    """This class represents the behavior of a classical arcade
    machine in the application."""

    def __init__(self, material: str, dimensions: list, weight: float, power_consumption: float,
                  memory: int, processors: str, base_price: float, color: str, make_vibration: bool, sound_record_alert: bool):
        
        super.__init__(material,dimensions,weight,power_consumption,memory,processors,base_price)
        self.color = color
        self.__make_vibration = make_vibration
        self.__sound_record_alert = sound_record_alert

    def add_videogame(self, videogame: VideoGame):
        """This method adds a videogame to the current Classical Arcade machine.

        In this method a videogame is received as argument,
        following a VideoGame abstract data type, and it is 
        add to internal games list.

        Args:
            videogame (VideoGame): videogame to be added
        """
        if videogame.get_category=="classical":
            self.__videogames.append(videogame)
        else:
            print(f"The videogame can not be added because its category is not compatible")

    def __str__(self) -> str:
        vibration=""
        if self.__make_vibration==True:
            vibration="Yes"
        else:
            vibration="No"
        
        alert=""
        if self.__sound_record_alert==True:
            alert="Yes"
        else:
            alert="No"

        temp_videogames = ""
        for vg in self.__videogames:
            temp_videogames += str(vg) + "\n"
        
        return (
            f"{'*' * 15}\n"
            f"Material: {self.material}\n"
            f"Color: {self.color}\n"
            f"Dimensions: {self.__dimensions} cm\n"
            f"Weight: {self.__weight} kg\n"
            f"Power Consumption: {self.__power_consumption} W\n"
            f"Memory: {self.__memory} MB\n"
            f"Processors: {self.__processors}\n"
            f"Vibration: {vibration}\n"
            f"Sound Record Alert: {alert}\n"
            f"Base Price: ${self.__base_price:.2f}\n"
            f"Videogames:\n{temp_videogames if temp_videogames else 'No videogames installed'}"
            )
    
class ShootingMachine(Machine):
    def __init__(self, material: str, dimensions: list, weight: float, power_consumption: float,
                 memory: int, processors: str, base_price: float, color: str, number_of_guns: int, 
                 gun_type: str, gun_accuracy: float, reload_mechanism: str, safety_lock: bool):
        
        super().__init__(material, dimensions, weight, power_consumption, memory, processors, base_price)
        self.color = color
        self.__number_of_guns = number_of_guns
        self.__gun_type = gun_type
        self.__gun_accuracy = gun_accuracy
        self.__reload_mechanism = reload_mechanism
        self.__safety_lock = safety_lock

    def add_videogame(self, videogame: VideoGame):
        """This method adds a videogame to the current Classical Arcade machine.

        In this method a videogame is received as argument,
        following a VideoGame abstract data type, and it is 
        add to internal games list.

        Args:
            videogame (VideoGame): videogame to be added
        """
        if videogame.get_category=="shooter":
            self.__videogames.append(videogame)
        else:
            print(f"The videogame can not be added because its category is not compatible")

    def __str__(self) -> str:
        safety_lock_str = "Yes" if self.__safety_lock else "No"
        temp_videogames = ""
        for vg in self.__videogames:
            temp_videogames += str(vg) + "\n"
        return (
            f"{'*' * 15}\n"
            f"Material: {self.material}\n"
            f"Color: {self.color}\n"
            f"Dimensions: {self.__dimensions} cm\n"
            f"Weight: {self.__weight} kg\n"
            f"Power Consumption: {self.__power_consumption} W\n"
            f"Memory: {self.__memory} MB\n"
            f"Processors: {self.__processors}\n"
            f"Number of Guns: {self.__number_of_guns}\n"
            f"Gun Type: {self.__gun_type}\n"
            f"Gun Accuracy: {self.__gun_accuracy}%\n"
            f"Reload Mechanism: {self.__reload_mechanism}\n"
            f"Safety Lock: {safety_lock_str}\n"
            f"Base Price: ${self.__base_price:.2f}\n"
            f"Videogames:\n{temp_videogames if temp_videogames else 'No videogames installed'}"
        )
    
class RacingMachine(Machine):
    def __init__(self, material: str, dimensions: list, weight: float, power_consumption: float,
                 memory: int, processors: str, base_price: float, color: str, wheel_type: str, 
                 pedal_sensitivity: float, seat_type: str, has_vibration: bool):
        
        super().__init__(material, dimensions, weight, power_consumption, memory, processors, base_price)
        self.color = color
        self.__wheel_type = wheel_type
        self.__pedal_sensitivity = pedal_sensitivity
        self.__seat_type = seat_type
        self.__has_vibration = has_vibration

    def add_videogame(self, videogame: VideoGame):
        """This method adds a videogame to the current Classical Arcade machine.

        In this method a videogame is received as argument,
        following a VideoGame abstract data type, and it is 
        add to internal games list.

        Args:
            videogame (VideoGame): videogame to be added
        """
        if videogame.get_category=="races":
            self.__videogames.append(videogame)
        else:
            print(f"The videogame can not be added because its category is not compatible")

    def __str__(self) -> str:
        vibration_str = "Yes" if self.__has_vibration else "No"
        temp_videogames = ""
        for vg in self.__videogames:
            temp_videogames += str(vg) + "\n"
        return (
            f"{'*' * 15}\n"
            f"Material: {self.material}\n"
            f"Color: {self.color}\n"
            f"Dimensions: {self.__dimensions} cm\n"
            f"Weight: {self.__weight} kg\n"
            f"Power Consumption: {self.__power_consumption} W\n"
            f"Memory: {self.__memory} MB\n"
            f"Processors: {self.__processors}\n"
            f"Wheel Type: {self.__wheel_type}\n"
            f"Pedal Sensitivity: {self.__pedal_sensitivity}%\n"
            f"Seat Type: {self.__seat_type}\n"
            f"Has Vibration: {vibration_str}\n"
            f"Base Price: ${self.__base_price:.2f}\n"
            f"Videogames:\n{temp_videogames if temp_videogames else 'No videogames installed'}"
        )

class VirtualReality(Machine):
    def __init__(self, material: str, dimensions: list, weight: float, power_consumption: float,
                 memory: int, processors: str, base_price: float, color: str, glasses_type: str, 
                 glasses_resolution: str, glasses_price: float):
        
        super().__init__(material, dimensions, weight, power_consumption, memory, processors, base_price)
        self.color = color
        self.__price = base_price + glasses_price
        self.__glasses_type = glasses_type
        self.__glasses_resolution = glasses_resolution
        self.__glasses_price = glasses_price

    def add_videogame(self, videogame: VideoGame):
        """This method adds a videogame to the current Classical Arcade machine.

        In this method a videogame is received as argument,
        following a VideoGame abstract data type, and it is 
        add to internal games list.

        Args:
            videogame (VideoGame): videogame to be added
        """
        if videogame.get_category=="vr":
            self.__videogames.append(videogame)
        else:
            print(f"The videogame can not be added because its category is not compatible")

    def __str__(self) -> str:
        temp_videogames = ""
        for vg in self.__videogames:
            temp_videogames += str(vg) + "\n"
        return (
            f"{'*' * 15}\n"
            f"Material: {self.material}\n"
            f"Color: {self.color}\n"
            f"Dimensions: {self.__dimensions} cm\n"
            f"Weight: {self.__weight} kg\n"
            f"Power Consumption: {self.__power_consumption} W\n"
            f"Memory: {self.__memory} GB\n"
            f"Processors: {self.__processors}\n"
            f"Glasses Type: {self.__glasses_type}\n"
            f"Glasses Resolution: {self.__glasses_resolution}\n"
            f"Glasses Price: {self.__glasses_price:.2f}\n"
            f"Base Price: ${self.__base_price:.2f}\n"
            f"Videogames:\n{temp_videogames if temp_videogames else 'No videogames installed'}"
        )

