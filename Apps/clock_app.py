from tkinter import Toplevel,Tk, PhotoImage, Label
from time import strftime

class clock_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock")
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
        root.title("Clock")
        root.resizable(False,False)
        photo = PhotoImage(master=root, file="Assets/clock.png")
        root.iconphoto(False,photo)
        time_lab=Label(root,font=("yellow",50),bg="yellow")
        time_lab.pack()
        day_lab=Label(root,font=("arial",40))
        day_lab.pack()
        date_lab=Label(root,font=("arial",40),bg="yellow")
        date_lab.pack()
        update()
        root.mainloop()

       

def open_clock():
    clock = Toplevel()
    app = clock_app(clock)

if __name__ == "__main__":
    root = Tk()
    app = clock_app(root)
    root.mainloop()
