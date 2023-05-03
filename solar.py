import tkinter as tk
import csv 
from tkinter import messagebox

class solarWindow:
    def __init__(self, master):
        self.master = master
        master.title("Explore Solar Options")

        self.label = tk.Label(master, text="Enter a State for the Average \n Electricity Estimate with Solar Energy:")
        self.label.pack(pady=20)

        state_entry = tk.Entry(master)
        state_entry.pack()

        search_button = tk.Button(master, text="Search", command=lambda: search_solar(self, state_entry))
        search_button.pack() 

        self.label = tk.Label(master, text="Average Electricity estimate (kWH):")
        self.label.pack(pady=20) 

        master.mainloop()
def search_solar(self, state_entry):
    state = state_entry.get()

    with open('solar.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['State'] == state:
                avg_rate_kwh = row['Rate per KWh']
                self.label.config(text=f"Average Electricity estimate (kWH): {avg_rate_kwh}")
                self.label.pack(pady=20)
                return

        self.label.config(text=f"{state} not found in CSV file")

