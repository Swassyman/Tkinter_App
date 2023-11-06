from tkinter import 

class notes_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Notes")
        
        # Create widgets for the second window
        # from here
        

       

def open_notes():
    note = tk.Toplevel()
    app = notes_app(note)

if __name__ == "__main__":
    root = tk.Tk()
    app = notes_app(root)
    root.mainloop()
