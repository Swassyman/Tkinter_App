from tkinter import 

class calc_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        # Create widgets for the second window
        # from here
        

       

def open_calculator():
    calc = tk.Toplevel()
    app = calc_app(calc)

if __name__ == "__main__":
    root = tk.Tk()
    app = calc_app(root)
    root.mainloop()
