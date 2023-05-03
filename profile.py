import tkinter as tk
import csv
from tkinter import messagebox

class profileWindow:
    def __init__(self, master):
        self.master = master
        master.title("Personalized Profile")

        self.label = tk.Label(master, text="Enter this month's Electricity Total:")
        self.label.pack(pady=20)

        self.state_entry = tk.Entry(master)
        self.state_entry.pack()

        search_button = tk.Button(master, text="Input", command=self.save_to_csv)
        search_button.pack()

        master.mainloop()
    def save_to_csv(self):
        value = self.state_entry.get()

        with open('profile.csv', mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([value])

        self.label.config(text=f"Enter this month's Electricity Total:")
        self.label.pack(pady=20)

        try:
            with open('profile.csv', mode='r', newline='') as csv_file:
                reader = csv.reader(csv_file)

                next(reader)

                values = [float(row[0]) for row in reader if row]

                if not values:
                    raise ValueError("CSV file is empty")

                total = sum(values)

                new_average = total / len(values)

                self.label = tk.Label(self.master, text=f"Estimate Total for next monthh:$ {new_average}")
                self.label.pack(pady=20)

                self.label.pack(pady=20)
        except (FileNotFoundError, ZeroDivisionError, ValueError) as e:
            messagebox.showerror("Error", f"Could not calculate new average: {str(e)}")
        