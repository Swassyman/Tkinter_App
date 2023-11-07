from tkinter import Tk,Button, PhotoImage
import Apps

def main():
    root = Tk()
    #Icons
    root_icon = PhotoImage(file="Assets/app_launcher_icon.png")
    #main root properties
    
    
    root.title("App Launcher")
    root.geometry("700x500")
    root.resizable(False,False)
    root.configure(bg="#49de71")
    root.iconphoto(False,root_icon)
    
    #Functions for each app added
    

    #Icons
    
    
    #Buttons to open each app
    # notes_button = Button(root,text="Notes",command = open_notes)
    # notes_button.place(x=5,y=5)
    # notes_button.config(height=20,width=30)
        
    calendar_button = Button(root, text="Clock",command = Apps.open_clock)
    calendar_button.place(x=239,y=5)
    calendar_button.config(height=20,width=30)

    calculator_button = Button(root,text="Calculator",command = Apps.open_calc)
    calculator_button.config(height=20,width=30)
    calculator_button.place(x=472,y=5)

    root.mainloop()
    
if __name__ == "__main__":
    main()