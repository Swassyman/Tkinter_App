import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Notepad")

# Create a text widget for text input
text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack(fill=tk.BOTH, expand=True)

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create a variable to store the current file
current_file = None

# Function to open a file
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

# Function to save a file
def save_file():
    global current_file
    if current_file:
        content = text_widget.get(1.0, tk.END)
        with open(current_file, "w") as file:
            file.write(content)
    else:
        save_file_as()

file_menu.add_command(label="Save", command=save_file)

# Function to save a file as a new file
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

# Function to exit the application
def exit_app():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.destroy()

file_menu.add_command(label="Exit", command=exit_app)

# Create an Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Function to cut selected text
def cut():
    text_widget.event_generate("<<Cut>>")

edit_menu.add_command(label="Cut", command=cut)

# Function to copy selected text
def copy():
    text_widget.event_generate("<<Copy>>")

edit_menu.add_command(label="Copy", command=copy)

# Function to paste copied/cut text
def paste():
    text_widget.event_generate("<<Paste>>")

edit_menu.add_command(label="Paste", command=paste)

# Function to undo the last action
def undo():
    text_widget.event_generate("<<Undo>>")

edit_menu.add_command(label="Undo", command=undo)

# Function to redo the last undone action
def redo():
    text_widget.event_generate("<<Redo>>")

edit_menu.add_command(label="Redo", command=redo)

# Create a Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Function to display information about the application
def about():
    messagebox.showinfo("About Notepad", "A simple Notepad application created using Python and Tkinter.")

help_menu.add_command(label="About", command=about)

# Run the main loop
root.mainloop()
