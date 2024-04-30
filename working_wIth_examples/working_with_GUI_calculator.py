# working_with_GUI_calculator
# An attempt to make a GUI calculator
import customtkinter
from tkinter import ttk

# Define function to perform operation on two operators
# <to be written>

# Define GUI
# start by setting up root window object
root = customtkinter.CTk() # root window object
root.title="Calculator"
root.geometry("500x400")
# Frame for buttons
frmButton = customtkinter.CTkFrame(master=root, width=20, height = 100, bg_color="red" )
frmButton.grid(row=1, column=1, padx=4,)

# Styles
# Create the object that contains the styles
objStyle=ttk.Style(frmButton)
# Now create a style
# New style called btn from default style for buttons called Tbutton
objStyle.configure('btn.Tbutton',
                font=('calibri,20'),
                weight="bold"               
)

# Add a text widget for the answer under root window
answer = customtkinter.CTkTextbox(master = root, width = 480, height = 20,)
# Place The Answer text widget
answer.grid(row=0,column=0, padx=4, pady=4,columnspan=5, )

# Create the tape widgit for the paper tape
tape = customtkinter.CTkTextbox(master=root, width=200, height=200)
# Place the tape widit 
tape.grid(row=1,column=0, padx=4,pady=4,rowspan=4)

# Create the buttons
btnPlus=ttk.Button(master=frmButton, style='btn.Tbutton', text = "+")
btnPlus.grid(row=1,column=1,padx=4,pady=4)

btnMinus=customtkinter.CTkButton(master = frmButton, width=40, height=40,text = "-")
btnMinus.grid(row=2,column=1,padx=4,pady=4)

btnTimes=customtkinter.CTkButton(master = frmButton, width=40, height=40,text = "*")
btnTimes.grid(row=3,column=1,padx=4,pady=4)

btnDivide=customtkinter.CTkButton(master = frmButton, width=40, height=40,text = "/")
btnDivide.grid(row=4,column=1,padx=4,pady=4)


# ********* Program Starts Here *******************

# start the TKinter main loop
root.mainloop()
#
print(f"Program Ends...")