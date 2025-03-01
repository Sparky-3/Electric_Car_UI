from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get()) #grabs whatever is in feet and turns it into a decimal
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0) #sets the textvarible meters to the value calculated
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters") #creates the window and titles it

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))  #creates the grid to place widgets into 
root.columnconfigure(0, weight=1) #tells tk to expand the grid to fill the window
root.rowconfigure(0, weight=1) #same as above

feet = StringVar() #allows tk to automatically update any text associated with this variable
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet) #creates a label and updates the varible feet to contain whatever is inside the entry
feet_entry.grid(column=2, row=1, sticky=(W, E)) # places the varible in the second column, first row and makes it cling to the southeast side

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E)) #creates a label with meters as its text, which automatically updates to display meters whenever meters is changed.

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5) #adds padding to all widgets

feet_entry.focus() #makes the cursor start on the entry space for feet
root.bind("<Return>", calculate) #tells Tk to run calculate if the user hits enter on their keyboard

root.mainloop() #starts the program
