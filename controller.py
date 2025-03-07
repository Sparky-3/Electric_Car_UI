from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Electric Car Controller')
root.geometry("600x600")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

spe_total = StringVar(value='0')
dis_total = StringVar(value='0')

def sub(total):
    try:
        value = int(total.get())
        if value > 0:
            total.set(value - 1)
    except ValueError:
        pass

def add(total):
    try:
        value = int(total.get())
        total.set(value + 1)
    except ValueError:
        pass

def layout(parent, title, total):
    ttk.Label(parent, text=title).grid(column=2, row=0, sticky='nsew', padx=5, pady=5)
    ttk.Button(parent, text='Decrease', command=lambda: sub(total)).grid(column=0, row=1, sticky='nsew', padx=5, pady=5)
    ttk.Button(parent, text='Increase', command=lambda: add(total)).grid(column=4, row=1, sticky='nsew', padx=5, pady=5)
    ttk.Label(parent, textvariable=total).grid(column=2, row=2, sticky='nsew', padx=5, pady=5)

def config(parent, col_num, row_num, col_weight, row_weight):
    for i in range(col_num):
        parent.columnconfigure(i, weight=col_weight)
    for i in range(row_num):
        parent.rowconfigure(i, weight=row_weight)

content = ttk.Frame(root)
content.grid(column=0, row=0, sticky='nsew')
content.columnconfigure(0, weight=1)
content.rowconfigure(0, weight=1)

mainframe = ttk.Frame(content, borderwidth=5, relief='ridge')
mainframe.grid(column=0, row=0, sticky='nsew')
mainframe.grid_propagate(False)

config(mainframe, 1, 2, 1, 1)

topframe = ttk.Frame(mainframe, borderwidth=5, relief='ridge')
bottomframe = ttk.Frame(mainframe, borderwidth=5, relief='ridge')

topframe.grid(column=0, row=0, sticky='nsew', padx=5, pady=5)
bottomframe.grid(column=0, row=1, sticky='nsew', padx=5, pady=5)

config(topframe, 5, 3, 1, 1)
config(bottomframe, 5, 3, 1, 1)

layout(topframe, 'Speed', spe_total)
layout(bottomframe, 'Distance', dis_total)

root.mainloop()

