import tkinter as tk



def resize_text_widget(event):
    # Get the current width and height of the frame
    frame_width = event.width
    frame_height = event.height
    
    # Calculate the new width and height for the text widget (50% of frame)
    new_width = int(frame_width * 0.65)
    new_height = int(frame_height * 0.58)
    
    # Update the text widget size
    data.config(width=new_width // 5, height=new_height // 10)  # Adjust for character size

# Create the main application window
root = tk.Tk()
root.title("Centered Text Widget Example")

# Set the size of the window
root.geometry("600x400")  # Set the window size (width x height)

# Create a frame to hold the text widget
Frame_right = tk.Frame(root)
Frame_right.pack(fill=tk.BOTH, expand=True)

Inventory_label = tk.Label(Frame_right, text="Inventory",font =('Helvetica', 28), width=20, height=2, bg = '#ffffff')
Inventory_label.grid(row =1, column =1)


# Create a text widget with a background color
data = tk.Text(Frame_right, bg="lightblue", fg="black")  # Light blue background
data.grid(row=2, column=1, sticky="ew")  # Fill the grid cell

# Bind the frame's resize event to update the text widget size
Frame_right.bind("<Configure>", resize_text_widget)

# Start the Tkinter event loop
root.mainloop()






