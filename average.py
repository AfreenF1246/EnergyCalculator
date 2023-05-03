import tkinter as tk
import csv 

class averageWindow:
    def __init__(self, master):
        self.master = master
        master.title("Average Electricity Bill By State")

        self.label = tk.Label(master, text="Enter a State:")
        self.label.pack(pady=20)

        state_entry = tk.Entry(master)
        state_entry.pack()

        search_button = tk.Button(master, text="Search", command=lambda: search_name(self, state_entry))
        search_button.pack() 
        
        self.label = tk.Label(master, text="Averages: ")
        self.label.pack(pady=20) 

        master.mainloop()

def search_name(self, state_entry):
    state = state_entry.get()

    with open('average.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['State'] == state:
                avg_rate_kwh = row['Rate per kWh']
                avg_per_month = row['Avg. bill']
                self.label.config(text=f"Average rate kWh: {avg_rate_kwh}")
                self.label.pack(pady=20)
                self.label = tk.Label(self.master, text=f"Average Per Month:${avg_per_month}")
                self.label.pack(pady=20)
                return

        self.label.config(text=f"{state} not found in CSV file")

#if __name__ == '__main__':
    #root = tk.Tk()
    #app = averageWindow(root)
    #root.mainloop()