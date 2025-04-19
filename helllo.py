from tkinter import *

root = Tk()
root.geometry("400x400")  # Set the window size

# Create a top frame for the top two quadrants
top_frame = Frame(root)
top_frame.pack(side=TOP, fill=BOTH, expand=True)

# Create a bottom frame for the bottom two quadrants
bottom_frame = Frame(root)
bottom_frame.pack(side=TOP, fill=BOTH, expand=True)

# Create the left frame for the top-left quadrant
frame1 = Frame(top_frame, bg="red")
frame1.pack(side=LEFT, fill=BOTH, expand=True)

# Create the right frame for the top-right quadrant
frame2 = Frame(top_frame, bg="green")
frame2.pack(side=LEFT, fill=BOTH, expand=True)

# Create the left frame for the bottom-left quadrant
frame3 = Frame(bottom_frame, bg="blue")
frame3.pack(side=LEFT, fill=BOTH, expand=True)

# Create the right frame for the bottom-right quadrant
frame4 = Frame(bottom_frame, bg="yellow")
frame4.pack(side=LEFT, fill=BOTH, expand=True)

root.mainloop()
