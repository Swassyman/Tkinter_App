from tkinter import Tk,Toplevel,Button, PhotoImage

root = Tk()
#Icons
root_icon = PhotoImage(file="Assets/app_launcher_icon.png")
calc_icon = PhotoImage(file = "Assets/calculator-icon.png")
#main root properties


root.title("App Launcher")
root.geometry("700x500")
root.resizable(False,False)
root.configure(bg="#49de71")
root.iconphoto(False,root_icon)

#Functions for each app added

def open_calculator():
    calculator = Toplevel(root)
    calculator.iconphoto(False,calc_icon)
    calculator.mainloop()
    
def open_calendar():
    calendar = Toplevel(root)
    calendar.mainloop()
    
def open_notes():
    notes = Toplevel(root)
    notes.mainloop()

#Icons
root_icon = PhotoImage(file="Assets/app_launcher_icon.png")


#Buttons to open each app
notes_button = Button(root,text="Notes",command = open_notes)
notes_button.place(x=5,y=5)
notes_button.config(height=20,width=30)

calendar_button = Button(root, text="Calendar",command = open_calendar)
calendar_button.place(x=239,y=5)
calendar_button.config(height=20,width=30)

calculator_button = Button(root,text="Calculator",command = open_calculator)
calculator_button.config(height=20,width=30)
calculator_button.place(x=472,y=5)

root.mainloop()