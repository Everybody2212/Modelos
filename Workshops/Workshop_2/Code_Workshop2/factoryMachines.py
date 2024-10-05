"""
This module has a class to define the factory machine interface.

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
from machines import DanceRevolution, ClassicalArcade, Machine, ShootingMachine, RacingMachine, VirtualReality

class FactoryMachines(ABC):
    """Abstract Base Class for Factory Machines.

    This class defines the interface for creating different types of 
    arcade machines. Subclasses must implement the create_machine 
    method to instantiate specific machine types.
    """

    @abstractmethod
    def create_machine(self, category: str, color: str, material: str) -> Machine:
        """Creates an arcade machine based on the specified category.

        Args:
            category (str): The category of the machine (e.g., 'dance', 'classical').
            color (str): The color of the machine.
            material (str): The material used to construct the machine.

        Returns:
            Machine: An instance of the specified machine type.

        Raises:
            NotImplementedError: If not implemented by the subclass.
        """
        pass

class PredefinedMachines(FactoryMachines):
    """Concrete Factory for Creating Predefined Arcade Machines.

    This factory creates instances of different predefined arcade machines 
    based on the category provided.
    """
    
    def create_machine(self, category: str, color: str, material: str) -> Machine:
        """Create predefined arcade machines based on category.

        Args:
            category (str): The category of the machine (e.g., 'dance', 'classical', 
                            'shooter', 'races', 'vr').
            color (str): The color of the machine.
            material (str): The material used to construct the machine.

        Returns:
            Machine: An instance of the specified arcade machine.

        Raises:
            ValueError: If the provided category does not exist.
        """
        if category == "dance":
            danceMachine = DanceRevolution(
                material,
                [270, 245, 250], 
                370,           
                750,            
                512,            
                "PowerPC",      
                3000,          
                color,           
                ["easy", "medium", "hard"],  
                ["up", "right", "down", "left"],  
                400              
            )
            danceMachine.adjustmentsByMaterial()
            return danceMachine

        elif category == "classical":
            classicalMachine = ClassicalArcade(
                material,
                [65, 50, 170],  
                70,          
                200,        
                16,           
                "SH-2",       
                500,         
                color,          
                True,           
                True          
            ) 
            classicalMachine.adjustmentsByMaterial()
            return classicalMachine

        elif category == "shooter":
            shooterMachine = ShootingMachine(
                material,
                [75, 100, 200], 
                100,           
                300,          
                512,            
                "ARM Cortex",   
                3000,      
                color,        
                2,           
                "rifle",     
                1,              
                "automatic",    
                True           
            )
            shooterMachine.adjustmentsByMaterial()
            return shooterMachine

        elif category == "races":
            racesMachine = RacingMachine(
                material,
                [120, 150, 180], 
                150,            
                250,             
                1024,             
                "MIPS R3000/R4000", 
                3000,           
                color,          
                "high pressure",  
                85,              
                "Sports seat",  
                True             
            ) 
            racesMachine.adjustmentsByMaterial()
            return racesMachine

        elif category == "vr":
            vrMachine = VirtualReality(
                material,
                [150, 200, 250], 
                250,           
                1200,         
                512,            
                "Intel Core i7",
                7500,           
                color,          
                "Oculus Rift S", 
                "2560 x 1440",   
                600            
            )
            vrMachine.adjustmentsByMaterial()
            return vrMachine

        else:
            raise ValueError("The category doesn't exist")
