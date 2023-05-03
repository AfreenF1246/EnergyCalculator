import tkinter as tk

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Main Window")

        # Create a label in the main window
        self.label = tk.Label(master, text="This is the main window!")
        self.label.pack(pady=20)

        # Create a button that opens a new window
        self.new_window_button = tk.Button(master, text="Open New Window", command=self.open_new_window)
        self.new_window_button.pack(pady=20)

    def open_new_window(self):
        # Create a new window
        new_window = tk.Toplevel(self.master)
        new_window.title("New Window")

        # Create a label in the new window
        label = tk.Label(new_window, text="This is a new window!")
        label.pack(pady=20)
