from tkinter import*
from time import*

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
photo=PhotoImage(file="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRx69jQE6C6AN0iUldsqW0hPXbiqG3oRlvNAYs14g6jTy6E42zJaJ1xa5sPbqmrJeggi5U&usqp=CAU")
window.iconphoto(False,photo)
time_lab=Label(window,font=("yellow",50),bg="yellow")
time_lab.pack()
day_lab=Label(window,font=("arial",40))
day_lab.pack()
date_lab=Label(window,font=("arial",40),bg="yellow")
date_lab.pack()
update()




window.mainloop()