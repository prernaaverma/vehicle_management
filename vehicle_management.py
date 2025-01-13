import tkinter as tk
from tkinter import ttk, messagebox
import json

# Base data for vehicles
VEHICLE_DATA = {
    "Car": {"brand": "Toyota", "model": "Corolla", "number_of_doors": 4},
    "Truck": {"brand": "Ford", "model": "F-150", "payload_capacity": 2.5},
    "Motorcycle": {"brand": "Harley-Davidson", "model": "Street 750", "has_sidecar": True},
}

class VehicleApp:
    def __init__(self, root):  # Correct constructor with self and root argument
        self.root = root
        self.root.title("Vehicle Management System")
        self.root.geometry("400x300")
        
        self.selected_vehicle_type = tk.StringVar()
        self.vehicle_details = {}
        
        self.setup_first_page()
    
    def setup_first_page(self):
        """First page: Select vehicle type."""
        self.clear_window()
        
        label = tk.Label(self.root, text="Select Vehicle Type", font=("Arial", 16))
        label.pack(pady=20)
        
        for vehicle_type in VEHICLE_DATA.keys():
            ttk.Radiobutton(
                self.root,
                text=vehicle_type,
                variable=self.selected_vehicle_type,
                value=vehicle_type
            ).pack(anchor=tk.W, padx=20)
        
        next_button = ttk.Button(self.root, text="Next", command=self.show_vehicle_details)
        next_button.pack(pady=20)
    
    def show_vehicle_details(self):
        """Show vehicle details based on the selected type."""
        vehicle_type = self.selected_vehicle_type.get()
        if not vehicle_type:
            messagebox.showerror("Error", "Please select a vehicle type.")
            return
        
        self.vehicle_details = VEHICLE_DATA[vehicle_type]
        self.setup_second_page()
    
    def setup_second_page(self):
        """Second page: Display and edit vehicle details."""
        self.clear_window()
        
        tk.Label(self.root, text="Vehicle Details", font=("Arial", 16)).pack(pady=10)
        
        fields = ["License Number", "Make", "Model", "Year"]
        self.entries = {}
        
        # Dynamically add fields based on vehicle type details
        for field in fields:
            frame = tk.Frame(self.root)
            frame.pack(pady=5, padx=10, fill=tk.X)
            
            tk.Label(frame, text=field, width=15, anchor=tk.W).pack(side=tk.LEFT)
            entry = ttk.Entry(frame)
            entry.pack(side=tk.RIGHT, expand=True, fill=tk.X)
            
            # Pre-fill details based on selected vehicle type
            if field == "Make":
                entry.insert(0, self.vehicle_details.get("brand", ""))
            elif field == "Model":
                entry.insert(0, self.vehicle_details.get("model", ""))
            
            self.entries[field] = entry
        
        # Add additional fields based on vehicle type
        if "number_of_doors" in self.vehicle_details:
            frame = tk.Frame(self.root)
            frame.pack(pady=5, padx=10, fill=tk.X)
            tk.Label(frame, text="Number of Doors", width=15, anchor=tk.W).pack(side=tk.LEFT)
            entry = ttk.Entry(frame)
            entry.insert(0, str(self.vehicle_details["number_of_doors"]))
            entry.pack(side=tk.RIGHT, expand=True, fill=tk.X)
            self.entries["Number of Doors"] = entry
        
        elif "payload_capacity" in self.vehicle_details:
            frame = tk.Frame(self.root)
            frame.pack(pady=5, padx=10, fill=tk.X)
            tk.Label(frame, text="Payload Capacity", width=15, anchor=tk.W).pack(side=tk.LEFT)
            entry = ttk.Entry(frame)
            entry.insert(0, str(self.vehicle_details["payload_capacity"]))
            entry.pack(side=tk.RIGHT, expand=True, fill=tk.X)
            self.entries["Payload Capacity"] = entry
        
        elif "has_sidecar" in self.vehicle_details:
            frame = tk.Frame(self.root)
            frame.pack(pady=5, padx=10, fill=tk.X)
            tk.Label(frame, text="Has Sidecar", width=15, anchor=tk.W).pack(side=tk.LEFT)
            entry = ttk.Entry(frame)
            entry.insert(0, str(self.vehicle_details["has_sidecar"]))
            entry.pack(side=tk.RIGHT, expand=True, fill=tk.X)
            self.entries["Has Sidecar"] = entry
        
        # Buttons
        save_button = ttk.Button(self.root, text="Save", command=self.save_vehicle_data)
        save_button.pack(side=tk.LEFT, padx=20, pady=20)
        
        exit_button = ttk.Button(self.root, text="Exit", command=self.root.quit)
        exit_button.pack(side=tk.RIGHT, padx=20, pady=20)
    
    def save_vehicle_data(self):
        """Save vehicle data to a JSON file."""
        data_to_save = {field: entry.get() for field, entry in self.entries.items()}
        
        if not all(data_to_save.values()):
            messagebox.showerror("Error", "All fields are required.")
            return
        
        # Save to a JSON file
        with open("vehicle_data.json", "w") as file:
            json.dump(data_to_save, file, indent=4)
        
        messagebox.showinfo("Success", "Vehicle data saved successfully!")
        self.setup_first_page()
    
    def clear_window(self):
        """Clear the window."""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleApp(root)  # Create instance of VehicleApp
    root.mainloop()
