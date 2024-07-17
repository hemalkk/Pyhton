import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

# Sample event data
events = {
    4000: ["2000-11-17", "2024-11-17"],
    5000: ["2024-10-25", "2024-10-27"],
}

# Function to search for events based on EventID and date
def search_events():
    event_id = int(event_id_var.get())
    search_date = date_var.get()

    if event_id in events:
        if search_date in events[event_id]:
            result.set(f"Found EventID {event_id} Date {search_date}")
        else:
            result.set(f"Not Found EventID {event_id} Date {search_date}")
    else:
        result.set("Invalid EventID")

# Create the main window
root = tk.Tk()
root.title("Event Viewer")
root.geometry("300x250")
root.configure(bg="#f0f0f0")

# EventID dropdown
event_id_var = tk.StringVar()
event_id_label = tk.Label(root, text="EventID", bg="#f0f0f0", font=("Arial", 12))
event_id_label.pack(pady=5)
event_id_dropdown = ttk.Combobox(root, textvariable=event_id_var, font=("Arial", 10))
event_id_dropdown['values'] = [4000, 5000]
event_id_dropdown.pack(pady=5)

# Date picker
date_var = tk.StringVar()
date_label = tk.Label(root, text="Search Date From", bg="#f0f0f0", font=("Arial", 12))
date_label.pack(pady=5)
date_picker = DateEntry(root, textvariable=date_var, date_pattern='yyyy-mm-dd', font=("Arial", 10))
date_picker.pack(pady=5)

# Search and Exit buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

search_button = tk.Button(button_frame, text="Search", command=search_events, bg="#4CAF50", fg="white", font=("Arial", 10))
search_button.grid(row=0, column=0, padx=10)
exit_button = tk.Button(button_frame, text="Exit", command=root.quit, bg="#f44336", fg="white", font=("Arial", 10))
exit_button.grid(row=0, column=1, padx=10)

# Result label
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, bg="#f0f0f0", font=("Arial", 12))
result_label.pack(pady=10)

# Run the application
root.mainloop()
