#importing tkinter from library
import tkinter as tk
from tkinter import ttk

#Creating a function for the event
def on_select(event):

    #create an item object that obtains the value of the selected item.
    selected_item = event.widget.get()
    print("selected item:", selected_item)

#create the root object window 
root = tk.Tk()
root.title("Bella is sleepy")

#create an array of item
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

#Create the combo box object, put the object in the root wwindow and populate values.
combo_box = ttk.Combobox(root, values=items)

#The blind function will tie the selected item to the on_selected function.
combo_box.bind("<<ComboboxSelected>>", on_select)

#packing object to the screen with the Geometry manager
combo_box.pack()

#Keeping the window visible
root.mainloop()
