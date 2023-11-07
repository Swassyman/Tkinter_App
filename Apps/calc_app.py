from tkinter import *

class calc_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        root.destroy()
        # Create widgets for the second window
        # from here
        global expression
        expression=""
        
        #to update expression in text box
        def press(num):
            global expression
            expression = expression + str(num)
            equation.set(expression)
            
        def equalpress():
            try:
                global expression
                total = str(eval(expression))
                equation.set(total)
                expression=""
                
            except:
                equation.set(" error ")
                expression=""
        
        def clear():
            global expression
            expression = ""
            equation.set("")
            
        calculator=Tk()
        calculator.title("Calculator")
        calculator.configure(background="#07398a")
        calculator.geometry("350x300")
        calculator.resizable(False,False)
        photo = PhotoImage(master=calculator, file ="C:/Code/Tkinter_App/Assets/calculator-icon.png")
        calculator.iconphoto(False,photo)
        
        equation = StringVar()
        expression_field = Entry(calculator,textvariable=equation,width=30,font=('Arial', 20))
        expression_field.place(x=0,y=0)
        
        button7 = Button(calculator, text=' 7 ', fg='black', bg='#4287f5', 
                   command=lambda: press(7), height=2, width=10) 
        button7.place(x=5,y=55)

        button8 = Button(calculator, text=' 8 ', fg='black', bg='#4287f5', 
                   command=lambda: press(8), height=2, width=10) 
        button8.place(x=90,y=55)

        button9 = Button(calculator, text=' 9 ', fg='black', bg='#4287f5', 
                   command=lambda: press(9), height=2, width=10) 
        button9.place(x=175,y=55)
        
        button4 = Button(calculator, text=' 4 ', fg='black', bg='#4287f5', 
                   command=lambda: press(4), height=2, width=10) 
        button4.place(x=5,y=105)

        button5 = Button(calculator, text=' 5 ', fg='black', bg='#4287f5', 
                   command=lambda: press(5), height=2, width=10) 
        button5.place(x=90,y=105)

        button6 = Button(calculator, text=' 6 ', fg='black', bg='#4287f5', 
                   command=lambda: press(6), height=2, width=10) 
        button6.place(x=175,y=105)

        button1 = Button(calculator, text=' 1 ', fg='black', bg='#4287f5', 
                   command=lambda: press(1), height=2, width=10) 
        button1.place(x=5,y=155)

        button2 = Button(calculator, text=' 2 ', fg='black', bg='#4287f5', 
                   command=lambda: press(2), height=2, width=10) 
        button2.place(x=90,y=155)

        button3 = Button(calculator, text=' 3 ', fg='black', bg='#4287f5', 
                   command=lambda: press(3), height=2, width=10)  
        button3.place(x=175,y=155)

        button0 = Button(calculator, text=' 0 ', fg='black', bg='#4287f5', 
                   command=lambda: press(0), height=2, width=10) 
        button0.place(x=90,y=205)

        plus = Button(calculator, text=' + ', fg='black', bg='#4287f5', 
               command=lambda: press("+"), height=5, width=11)  
        plus.place(x=260,y=160)

        minus = Button(calculator, text=' - ', fg='black', bg='#4287f5', 
                       command=lambda: press("-"), height=3, width=11)
        minus.place(x=260,y=100)

        multiply = Button(calculator, text=' * ', fg='black', bg='#4287f5', 
                   command=lambda: press("*"), height=2, width=22) 
        multiply.place(x=5,y=255)

        divide = Button(calculator, text=' / ', fg='black', bg='#4287f5', 
                   command=lambda: press("/"), height=2, width=23) 
        #divide.grid(row=5, column=3) 
        divide.place(x=175,y=255)

        equal = Button(calculator, text=' = ', fg='black', bg='#4287f5', 
               command=equalpress, height=2, width=10) 
        #equal.grid(row=5, column=2) 
        equal.place(x=175,y=205)

        clear = Button(calculator, text='Clear', fg='black', bg='#4287f5', 
               command=clear, height=2, width=11) 
        #clear.grid(row=5, column='1')
        clear.place(x=260,y=55)

        Decimal= Button(calculator, text='.', fg='black', bg='#4287f5', 
                   command=lambda: press('.'), height=2, width=10) 
        #Decimal.grid(row=6, column=0) 
        Decimal.place(x=5,y=205)
        
        
        

       

def open_calc():
    calc = Toplevel()
    app = calc_app(calc)


if __name__ == "__main__":
    root = Tk()
    app = calc_app(root)
    root.mainloop()
