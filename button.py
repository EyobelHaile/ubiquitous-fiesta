#import tkinter from library
import tkinter as tk

#declare a function called button clicked then print
def button_click():
    print("Button clicked!")

#Create a root window   
root = tk.Tk()
root.title("Button Example")

#Create the button object
#call button subclass from the button library
button = tk.Button(root, text="Click Me!", command=button_click)
button.pack()

#keep the root window visible
root.mainloop()




