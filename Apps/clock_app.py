from tkinter import Toplevel,Tk, PhotoImage, Label
from time import strftime

class clock_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock")
        root.destroy()
        # Create widgets for the second clock
        # from here
        def update():
            time_str = strftime("%I : %M : %S :%p")
            time_lab.config(text=time_str)
            time_lab.after(1000,update)
            day_str = strftime("%A")
            day_lab.config(text=day_str)
            date_str = strftime("%d :%B:%Y")
            date_lab.config(text=date_str)
        clock = Tk()
        clock.title("clock")
        clock.resizable(False,False)
        photo = PhotoImage(master=clock, file="C:/Code/Tkinter_App/Assets/clock.png")
        clock.iconphoto(False,photo)
        time_lab=Label(clock,font=("yellow",50),bg="yellow")
        time_lab.pack()
        day_lab=Label(clock,font=("arial",40))
        day_lab.pack()
        date_lab=Label(clock,font=("arial",40),bg="yellow")
        date_lab.pack()
        update()
        clock.mainloop()

       

def open_clock():
    clock = Toplevel()
    app = clock_app(clock)

if __name__ == "__main__":
    root = Tk()
    app = clock_app(root)
    root.mainloop()
