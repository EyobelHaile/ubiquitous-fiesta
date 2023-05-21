#importing tkinter from library
import tkinter as tk
from tkinter import ttk

#Creating a function for the event
def on_select(event):

    #create an item object that obtains the value of the selected item.
    selected_item = event.widget.get()
    print("selected item:", selected_item)

#
root = tk.tk()
root.title("Bella is sleepy")

#create an array of item
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
#Create the combo box object, put the object in the root wwindow and populate values.
combo_box = ttk.Combobox(root, values=items)

combo_box.bind("<<ComboboxSelected>>", on_select)

combo_box.pack()

root.mainloop()