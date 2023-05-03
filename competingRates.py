import tkinter as tk
import csv 
from tkinter import messagebox

class ratesWindow:
    def __init__(self, master):
        self.master = master
        master.title("Competing Rate by State")

        self.label = tk.Label(master, text="Enter a state for a selection of \n competing rates for a selection of companies")
        self.label.pack(pady=20)

        state_entry = tk.Entry(master)
        state_entry.pack()

        search_button = tk.Button(master, text="Search", command=lambda: search_name(self, state_entry))
        search_button.pack()  
        #This should be changed based on recent price
        self.label = tk.Label(master, text="PSEG'S AVERAGE RESIDENTIAL PRICE PER KWH: (enter current rate)¢ ")
        self.label.pack(pady=20) 

        self.label = tk.Label(master, text="Average rate kWh (cents per kWh): ")

        self.label.pack(pady=20)
        master.mainloop()

def search_name(self, state_entry):
    state = state_entry.get()

    with open('competingRates.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['State'] == state:
                cents_per_kWH = row['Cents per kWh']
                self.label.config(text=f"Average rate kWh: {cents_per_kWH}¢")
                self.label.pack(pady=20)
                return

        self.label.config(text=f"{state} not found in CSV file")
