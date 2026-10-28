# Dynamic Interactive Image/File Viewer with Dialog Prompts
import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
from PIL import Image, ImageTk
import os

def open_file(event=None):
    path = filedialog.askopenfilename(
        filetypes=[
            ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"),
            ("Text files", "*.txt"),
            ("All files", "*.*")
        ]
    )

    if not path:
        return
    filename.config(text="File: " + os.path.basename(path))
    canvas.delete("all")

    try:
        if path.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
            img = Image.open(path)
            img.thumbnail((500, 350))
            photo = ImageTk.PhotoImage(img)
            canvas.image = photo
            canvas.create_image(250, 175, image=photo)
            messagebox.showinfo("Success", "Image opened successfully!")
        else:
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()

            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, content)
            messagebox.showinfo("Success", "Text file opened successfully!")
    except Exception as error:
        messagebox.showerror("Error", str(error))

def change_color():
    color = colorchooser.askcolor(title="Choose Background Color")[1]
    if color:
        root.config(bg=color)
        canvas.config(bg=color)
        messagebox.showinfo("Color", "Background color changed!")

def clear_view():
    canvas.delete("all")
    canvas.image = None
    text_area.delete("1.0", tk.END)
    filename.config(text="No file selected")

root = tk.Tk()
root.title("Interactive Image and File Viewer")
root.geometry("650x650")

tk.Label(root, text="Image and File Viewer",
         font=("Arial", 18, "bold")).pack(pady=10)

filename = tk.Label(root, text="No file selected")
filename.pack()

tk.Button(root, text="Open File", command=open_file).pack(pady=5)
tk.Button(root, text="Change Background Color",
          command=change_color).pack(pady=5)
tk.Button(root, text="Clear View", command=clear_view).pack(pady=5)

canvas = tk.Canvas(root, width=500, height=350, bg="white")
canvas.pack(pady=10)

text_area = tk.Text(root, height=8, width=70)
text_area.pack(pady=5)

root.bind("<Return>", open_file)
canvas.bind("<Button-1>", lambda event: change_color())

root.mainloop()