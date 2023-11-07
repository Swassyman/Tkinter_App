from tkinter import equation, Toplevel, Tk

class notes_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Notes")
        root.destroy()
        # Create widgets for the second window
        # from here

        
def open_notes():
    note = Toplevel()
    app = notes_app(note)

if __name__ == "__main__":
    root = Tk()
    app = notes_app(root)
    root.mainloop()
