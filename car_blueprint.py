import tkinter as tk

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed
    
    def get_details(self):
        return f"{self.__year_model} {self.__make}"
    

class CarDashboard:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Speedometer")
        self.main_window.geometry("350x300")
        self.main.window.configure(bg="lightble")
        self.my_car = Car("2026", "CyberTruck")
        