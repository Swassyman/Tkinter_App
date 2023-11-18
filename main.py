from tkinter import Tk,Button, Label,Canvas,NW
from PIL import ImageTk, Image 
import Apps

def main():
    root = Tk()
    #Icons
    root_icon = ImageTk.PhotoImage(file="Assets/app_launcher_icon.png")
    
    #main root properties
    root.title("App Launcher")
    root.geometry("700x500")
    root.resizable(False,False)
    root.configure(bg="#303e4c")
    root.iconphoto(False,root_icon)
    
    Label(root,text="AppLauncher",bg="#303e4c",fg="white",font=('Arial',25)).place(x=300,y=375)
    
    #Create a canvas
    canvas= Canvas(root, width= 100, height= 70, bg="#303e4c",highlightthickness=0)
    canvas.place(x=200,y=355)

#Load an image in the script
    img= (Image.open("Assets/app_launcher_icon.png"))

#Resize the Image using resize method
    resized_image= img.resize((80,70), Image.LANCZOS)
    new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
    canvas.create_image(10,10, anchor=NW, image=new_image)
    
    
    #Buttons to open each app
    notes_button = Button(root,text="Notes",command = Apps.open_notes)
    notes_button.place(x=5,y=5)
    notes_button.config(height=20,width=30)
        
    calendar_button = Button(root, text="Clock",command = Apps.open_clock)
    calendar_button.place(x=239,y=5)
    calendar_button.config(height=20,width=30)

    calculator_button = Button(root,text="Calculator",command = Apps.open_calc)
    calculator_button.config(height=20,width=30)
    calculator_button.place(x=472,y=5)
    
    

    root.mainloop()
    
if __name__ == "__main__":
    main()