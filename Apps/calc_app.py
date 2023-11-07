from tkinter import *

class calc_app:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        # Create widgets for the second window
        # from here
        
        self.expression=""
        self.equation = StringVar()
        self.expression_field = Entry(self.master, textvariable=self.equation, width=30, font=('Arial', 20))
        self.expression_field.place(x=0, y=0)
        
        #to update expression in text box
        def press(num):
            self.expression = self.expression + str(num)
            self.equation.set(self.expression)
            
        def equalpress():
            try:
                total = str(eval(self.expression))
                self.equation.set(total)
                self.expression=""
                
            except:
                self.equation.set(" error ")
                self.expression=""
        
        def clear():
            self.expression = ""
            self.equation.set("")
            
        
        master.configure(background="#07398a")
        master.geometry("350x300")
        master.resizable(False,False)
        photo = PhotoImage(master=master, file ="C:/Code/Tkinter_App/Assets/calculator-icon.png")
        master.iconphoto(False,photo)
        
        self.equation = StringVar()
        self.expression_field = Entry(master,textvariable=self.equation,width=30,font=('Arial', 20))
        self.expression_field.place(x=0,y=0)
        
        button7 = Button(master, text=' 7 ', fg='black', bg='#4287f5', 
                   command=lambda: press(7), height=2, width=10) 
        button7.place(x=5,y=55)

        button8 = Button(master, text=' 8 ', fg='black', bg='#4287f5', 
                   command=lambda: press(8), height=2, width=10) 
        button8.place(x=90,y=55)

        button9 = Button(master, text=' 9 ', fg='black', bg='#4287f5', 
                   command=lambda: press(9), height=2, width=10) 
        button9.place(x=175,y=55)
        
        button4 = Button(master, text=' 4 ', fg='black', bg='#4287f5', 
                   command=lambda: press(4), height=2, width=10) 
        button4.place(x=5,y=105)

        button5 = Button(master, text=' 5 ', fg='black', bg='#4287f5', 
                   command=lambda: press(5), height=2, width=10) 
        button5.place(x=90,y=105)

        button6 = Button(master, text=' 6 ', fg='black', bg='#4287f5', 
                   command=lambda: press(6), height=2, width=10) 
        button6.place(x=175,y=105)

        button1 = Button(master, text=' 1 ', fg='black', bg='#4287f5', 
                   command=lambda: press(1), height=2, width=10) 
        button1.place(x=5,y=155)

        button2 = Button(master, text=' 2 ', fg='black', bg='#4287f5', 
                   command=lambda: press(2), height=2, width=10) 
        button2.place(x=90,y=155)

        button3 = Button(master, text=' 3 ', fg='black', bg='#4287f5', 
                   command=lambda: press(3), height=2, width=10)  
        button3.place(x=175,y=155)

        button0 = Button(master, text=' 0 ', fg='black', bg='#4287f5', 
                   command=lambda: press(0), height=2, width=10) 
        button0.place(x=90,y=205)

        plus = Button(master, text=' + ', fg='black', bg='#4287f5', 
               command=lambda: press("+"), height=5, width=11)  
        plus.place(x=260,y=160)

        minus = Button(master, text=' - ', fg='black', bg='#4287f5', 
                       command=lambda: press("-"), height=3, width=11)
        minus.place(x=260,y=100)

        multiply = Button(master, text=' * ', fg='black', bg='#4287f5', 
                   command=lambda: press("*"), height=2, width=22) 
        multiply.place(x=5,y=255)

        divide = Button(master, text=' / ', fg='black', bg='#4287f5', 
                   command=lambda: press("/"), height=2, width=23) 
        #divide.grid(row=5, column=3) 
        divide.place(x=175,y=255)

        equal = Button(master, text=' = ', fg='black', bg='#4287f5', 
               command=equalpress, height=2, width=10) 
        #equal.grid(row=5, column=2) 
        equal.place(x=175,y=205)

        clear = Button(master, text='Clear', fg='black', bg='#4287f5', 
               command=clear, height=2, width=11) 
        #clear.grid(row=5, column='1')
        clear.place(x=260,y=55)

        Decimal= Button(master, text='.', fg='black', bg='#4287f5', 
                   command=lambda: press('.'), height=2, width=10) 
        #Decimal.grid(row=6, column=0) 
        Decimal.place(x=5,y=205)
        
        
        

       

def open_calc():
    calc = Toplevel()
    calc_app(calc)


if __name__ == "__main__":
    root = Tk()
    app = calc_app(root)
    root.mainloop()
