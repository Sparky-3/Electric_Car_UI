from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Electric Car Controller')

total = StringVar()
total.set('0')
def sub():
    try:
        if int(total.get()) <= 0:
            pass
        else:
            value = int(total.get())
            total.set(value = value - 1)

    except ValueError:
        pass
def add():
    try:
        value = int(total.get())
        total.set(value = value + 1)

    except ValueError:
        pass


def layout(self, title, total):
    ttk.Label(self, text=title).grid(column=3, row=1)
    ttk.Button(self, text='Decrease', command=sub).grid(column=1, row=2)
    ttk.Button(self, text='Increase', command=add).grid(column=4, row=2)
    ttk.Label(self, textvariable = total).grid(column=3, row=3)

boundry = ttk.Frame(root)
mainframe = ttk.Frame(boundry, borderwidth=5, relief='ridge')

boundry.grid(column=0,row=0)
mainframe.grid(column=0,row=0, columnspan=1, rowspan=2)

topframe = ttk.Frame(mainframe, borderwidth=5, relief='ridge', padding='3 3 12 12')
bottomframe = ttk.Frame(mainframe, borderwidth=5, relief='ridge', padding='3 3 12 12')

topframe.grid(column=1, row=1, columnspan=5, rowspan=4)


layout(topframe, 'Speed', total)

root.mainloop()
