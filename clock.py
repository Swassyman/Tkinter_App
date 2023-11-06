from tkinter import Tk,PhotoImage, Label
from time import strftime

def update():
    time_str = strftime("%I : %M : %S :%p")
    time_lab.config(text=time_str)
    time_lab.after(1000,update)
    day_str = strftime("%A")
    day_lab.config(text=day_str)
    date_str = strftime("%d :%B:%Y")
    date_lab.config(text=date_str)
window = Tk()
window.title("clock")
photo = PhotoImage(master=window, file="Assets/clock.png")
window.iconphoto(False,photo)
time_lab=Label(window,font=("yellow",50),bg="yellow")
time_lab.pack()
day_lab=Label(window,font=("arial",40))
day_lab.pack()
date_lab=Label(window,font=("arial",40),bg="yellow")
date_lab.pack()
update()




window.mainloop()