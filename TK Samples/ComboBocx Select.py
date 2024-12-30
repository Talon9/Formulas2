# Python program to get index of selected 
# option in Tkinter Combobox 

# Import the libraries tkinter 
from tkinter import *
from tkinter import ttk 

# Create a GUI app 
app = Tk() 

# Set the geometry of the app 
app.geometry("600x400") 

# Function to clear the Combobox 
def clear(): 
	combo.set('') 

# Function to print the index of selected option 
# in Combobox 
def get_index(*arg): 
	Label(app, text="The value at index " + str(combo.current()) +
		" is" + " " + str(var.get()), font=('Helvetica 12')).pack() 


# Define Tuple of months 
months = ('January', 'February', 'March', 'April', 'May', 'June', 
		'July', 'August', 'September', 'October', 'November', 
		'December') 

# Create a Combobox widget 
var = StringVar() 
combo = ttk.Combobox(app, textvariable=var) 
combo['values'] = months 
combo['state'] = 'readonly'
combo.pack(padx=5, pady=5) 

# Set the tracing for the given variable 
var.trace('w', get_index) 

# Create a button to clear the selected combobox 
# text value 
button = Button(app, text="Clear", command=clear) 
button.pack() 

# Make infinite loop for displaying app on 
# the screen 
app.mainloop() 
