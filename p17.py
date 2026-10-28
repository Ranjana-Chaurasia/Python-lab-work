# Multi-Functional Graphical Desktop Calculator
import tkinter as tk

def click(value):
    if value == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    elif value == "C":
        display.delete(0, tk.END)

    elif value == "⌫":
        display.delete(len(display.get()) - 1, tk.END)

    else:
        if display.get() == "Error":
            display.delete(0, tk.END)
        display.insert(tk.END, value)

root = tk.Tk()
root.title("Desktop Calculator")
root.geometry("320x400")
root.resizable(False, False)

display = tk.Entry(root, font=("Arial", 20), justify="right")
display.grid(row=0, column=0, columnspan=4,
             padx=10, pady=10, ipady=10, sticky="nsew")

buttons = [
    ("C", 1, 0), ("⌫", 1, 1), ("(", 1, 2), (")", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3)
]

for text, row, col in buttons:
    button = tk.Button(
        root, text=text, font=("Arial", 14),
        command=lambda value=text: click(value)
    )
    button.grid(row=row, column=col, padx=4, pady=4,
                ipadx=8, ipady=8, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()