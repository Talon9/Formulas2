from tkinter import *

root = Tk()
root.geometry("800x400") # x by y
root.title(" Import Directions ")

def btnCancel():
    print("Clicked")



def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    Output.delete
    if(INPUT == "120"):
        Output.insert(END, 'Correct')
    else:
        Output.insert(END, "Wrong answer")
    
lFormulas = Label(text = "Formulas").grid(row=1, column = 1)
#cboFormulas = Dropdown(root).grid(row=2, column = 1)

cancel = Button(root, text="Cancel", padx=10, command=btnCancel, bg="#FF99FF").grid(row=3, column = 1)

# txtFormula = Text(root, height = 10, width = 25, bg = "green").grid(row=2, column=3)

# lDirections = Label(text = "Directions").grid(row=5, column = 1)
# txtDirections = Text(root, height = 10, width = 25, bg = "grey").grid(row=6, column=4)

# Output = Text(root, height = 5, width = 25, bg = "light cyan").grid(row=4, column=3)
# Display = Button(root, height = 2, width = 20, text ="Show", command = lambda:Take_input()).grid(row=5, column=3)

mainloop()
