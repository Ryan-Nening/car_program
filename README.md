
# Car Program

**An Interactive OOP Digital Dashboard**

## Project Overview
This project is an interactive digital speedometer designed to showcase advanced **Encapsulation** mechanics through Mutator methods. 

Rather than executing an automated `for` loop to adjust the vehicle's speed, this program features a live, user-driven UI where the speed is dynamically manipulated via graphical "Accelerate" and "Brake" buttons.

## Core OOP Features
* **State Control:** The vehicle's `__speed` is strictly private and initialized at 0. It cannot be hardcoded or bypassed.
* **Controlled Mutators:** The only way to alter the speed state is through the `accelerate()` (+5) and `brake()` (-5) functions, ensuring strict logic enforcement.
* **Live Accessors:** The Tkinter GUI continuously calls the `get_speed()` method to instantly update the neon display without directly touching the private variables.

## How to Run the Program
1. Open the `car_program` folder in your terminal or IDE.
2. Run the main execution driver:
   ```bash
   python main_car_file.py
