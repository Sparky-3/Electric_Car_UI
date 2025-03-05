from tkinter import *
from tkinter import ttk

root = Tk()

def layout(self):
    ttk.Label(self, text='test').grid(column=3, row=1, sticky=N)

boundry = ttk.Frame(root)
mainframe = ttk.Frame(boundry, borderwidth=5, relief='ridge')

boundry.grid(column=0,row=0)
mainframe.grid(column=0,row=0, columnspan=1, rowspan=2, sticky=(N, W, E, S))

topframe = ttk.Frame(mainframe, borderwidth=5, relief='ridge', padding='3 3 12 12')
bottomframe = ttk.Frame(mainframe, borderwidth=5, relief='ridge', padding='3 3 12 12')

mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
topframe.grid(column=1, row=1, columnspan=5, rowspan=4)


layout(topframe)

root.mainloop()
