import tkinter as tk
from main_window import MainWindow
from average import averageWindow
from profile import profileWindow
from solar import solarWindow
from competingRates import ratesWindow

class WelcomePage:
    def __init__(self, master):
        self.master = master
        master.title("Welcome Page")

        self.welcome_label = tk.Label(master, text="Electricity Calculator", font=("Arial", 24))
        self.welcome_label.pack(pady=20)

        self.button1 = tk.Button(master, text="Average Electricity Bill By State", command=self.button1_click)
        self.button2 = tk.Button(master, text="Personalized Profile", command=self.button2_click)
        self.button3 = tk.Button(master, text="Explore Solar Options", command=self.button3_click)
        self.button4 = tk.Button(master, text="Competing Rate by State", command=self.button4_click)

        self.button1.pack(pady=10)
        self.button2.pack(pady=10)
        self.button3.pack(pady=10)
        self.button4.pack(pady=10)

    def button1_click(self):
        new_window = tk.Toplevel(self.master)
        averageWindow(new_window)

    def button2_click(self):
        new_window = tk.Toplevel(self.master)
        profileWindow(new_window)

    def button3_click(self):
        new_window = tk.Toplevel(self.master)
        solarWindow(new_window)

    def button4_click(self):
        new_window = tk.Toplevel(self.master)
        ratesWindow(new_window)
