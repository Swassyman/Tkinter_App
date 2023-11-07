import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
root.title("Notepad")

text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack(fill=tk.BOTH, expand=True)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

current_file = None

def open_file():
    global current_file
    file = filedialog.askopenfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        current_file = file.name
        content = file.read()
        text_widget.delete(1.0, tk.END)
        text_widget.insert(1.0, content)
        file.close()

file_menu.add_command(label="Open", command=open_file)

def save_file():
    global current_file
    if current_file:
        content = text_widget.get(1.0, tk.END)
        with open(current_file, "w") as file:
            file.write(content)
    else:
        save_file_as()

file_menu.add_command(label="Save", command=save_file)

def save_file_as():
    file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        global current_file
        current_file = file.name
        content = text_widget.get(1.0, tk.END)
        file.write(content)
        file.close()

file_menu.add_command(label="Save As", command=save_file_as)

file_menu.add_separator()

def exit_app():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.destroy()

file_menu.add_command(label="Exit", command=exit_app)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

def cut():
    text_widget.event_generate("<<Cut>>")

edit_menu.add_command(label="Cut", command=cut)

def copy():
    text_widget.event_generate("<<Copy>>")

edit_menu.add_command(label="Copy", command=copy)

def paste():
    text_widget.event_generate("<<Paste>>")

edit_menu.add_command(label="Paste", command=paste)

def undo():
    text_widget.event_generate("<<Undo>>")

edit_menu.add_command(label="Undo", command=undo)

def redo():
    text_widget.event_generate("<<Redo>>")

edit_menu.add_command(label="Redo", command=redo)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

def about():
    messagebox.showinfo("About Notepad", "A simple Notepad application created using Python and Tkinter.")

help_menu.add_command(label="About", command=about)

root.mainloop()
