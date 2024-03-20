import pandas as pd
import tkinter as tk
from tkinter import filedialog

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    return file_path

def save_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    return file_path

# Use the file dialog to select the stop_times.txt file
stop_times_file = select_file()

if stop_times_file:
    # Read the selected file
    stop_times = pd.read_csv(stop_times_file)

    # Filter rows where timepoint is 1
    timepoint_1 = stop_times[stop_times['timepoint'] == 1]

    # Prompt user to choose where to save the file
    save_path = save_file()
    if save_path:
        # Export to the chosen file
        timepoint_1.to_csv(save_path, index=False)
        print(f"File exported successfully to {save_path}")
    else:
        print("Save operation cancelled.")
else:
    print("File selection cancelled.")
