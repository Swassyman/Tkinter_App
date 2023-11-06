from tkinter import Tk, Toplevel

class calc_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        # Create widgets for the second window
        # from here
        

       

def open_calc():
    calc = Toplevel()
    app = calc_app(calc)

if __name__ == "__main__":
    root = Tk()
    app = calc_app(root)
    root.mainloop()
