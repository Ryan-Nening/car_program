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
        self.main_window.configure(bg="lightblue")
        self.my_car = Car("2026", "CyberTruck")

    def build_user_interface(self):
        tk.Label(self.main_window, text = f"Vehicle: {self.my_car.get_details()}", background = "#0b0c10", foreground = "#66fcf1", font = ("Helvetica", 14, "bold")).pack(pady = (20, 10))
        self.speed_label = tk.Label(self.main_window, text = str(self.my_car.get_speed()), font = ("Courier", 50, "bold"), background = "#0b0c10", foreground = "#45a29e")
        self.speed_label.pack(pady = 10)

        self.button_frame = tk.Frame(self.main_window, background = "#060c10")
        self.button_frame.pack(pady = 10)

        tk.Button(self.btn_frame, text="Accelerate (+5)", bg="#2c3e50", fg="white", width=12, command=self.press_accelerate).grid(row=0, column=0, padx=10)
        tk.Button(self.btn_frame, text="Brake (-5)", bg="#c0392b", fg="white", width=12, command=self.press_brake).grid(row=0, column=1, padx=10)

        