# GUI Student Record Manager with File Storage
import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os

records = []
filename = "students.json"

def add_record():
    if not name.get().strip() or not roll.get().strip():
        messagebox.showerror("Error", "Enter name and roll number!")
        return
    record = {
        "Name": name.get().strip(),
        "Roll No": roll.get().strip(),
        "Course": course.get(),
        "Gender": gender.get(),
        "Skills": ", ".join(
            skill for skill, var in skills.items() if var.get()
        ),
        "Address": address.get("1.0", tk.END).strip()
    }
    if any(r["Roll No"] == record["Roll No"] for r in records):
        messagebox.showerror("Error", "Roll number already exists!")
        return
    records.append(record)
    show_records()
    clear_fields()
    messagebox.showinfo("Success", "Student added successfully!")


def show_records():
    output.delete("1.0", tk.END)
    for r in records:
        output.insert(tk.END, str(r) + "\n\n")


def search_record():
    query = roll.get().strip()
    for r in records:
        if r["Roll No"] == query:
            output.delete("1.0", tk.END)
            output.insert(tk.END, str(r))
            return
    messagebox.showinfo("Search", "Student not found.")


def delete_record():
    query = roll.get().strip()
    for r in records:
        if r["Roll No"] == query:
            records.remove(r)
            show_records()
            messagebox.showinfo("Success", "Student deleted.")
            return
    messagebox.showinfo("Delete", "Student not found.")


def clear_fields():
    name.delete(0, tk.END)
    roll.delete(0, tk.END)
    address.delete("1.0", tk.END)
    gender.set("Female")
    course.set("B.Tech")
    for var in skills.values():
        var.set(False)


def save_file():
    path = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON files", "*.json")]
    )
    if path:
        with open(path, "w") as file:
            json.dump(records, file, indent=4)
        messagebox.showinfo("Success", "Records saved successfully!")


def load_file():
    global records
    path = filedialog.askopenfilename(
        filetypes=[("JSON files", "*.json")]
    )
    if path:
        try:
            with open(path, "r") as file:
                records = json.load(file)
            show_records()
            messagebox.showinfo("Success", "Records loaded successfully!")
        except (json.JSONDecodeError, OSError):
            messagebox.showerror("Error", "Unable to load this file.")


root = tk.Tk()
root.title("Student Record Manager")
root.geometry("700x650")

tk.Label(root, text="Student Record Manager",
         font=("Arial", 18, "bold")).grid(
    row=0, column=0, columnspan=4, pady=10
)
tk.Label(root, text="Name").grid(row=1, column=0, sticky="w", padx=10)
name = tk.Entry(root)
name.grid(row=1, column=1, sticky="ew", padx=5)

tk.Label(root, text="Roll Number").grid(row=2, column=0, sticky="w", padx=10)
roll = tk.Entry(root)
roll.grid(row=2, column=1, sticky="ew", padx=5)

tk.Label(root, text="Course").grid(row=3, column=0, sticky="w", padx=10)
course = tk.StringVar(value="B.Tech")
tk.OptionMenu(root, course, "B.Tech", "BCA", "MCA", "M.Tech").grid(
    row=3, column=1, sticky="ew", padx=5
)
tk.Label(root, text="Gender").grid(row=4, column=0, sticky="w", padx=10)
gender = tk.StringVar(value="Female")
gender_frame = tk.Frame(root)
gender_frame.grid(row=4, column=1, sticky="w")

for value in ["Female", "Male", "Other"]:
    tk.Radiobutton(gender_frame, text=value,
                   variable=gender, value=value).pack(side="left")

tk.Label(root, text="Skills").grid(row=5, column=0, sticky="w", padx=10)
skills = {s: tk.BooleanVar() for s in ["Python", "Java", "C++"]}
skill_frame = tk.Frame(root)
skill_frame.grid(row=5, column=1, sticky="w")

for skill, var in skills.items():
    tk.Checkbutton(skill_frame, text=skill, variable=var).pack(side="left")

tk.Label(root, text="Address").grid(row=6, column=0, sticky="nw", padx=10)
address = tk.Text(root, height=3, width=30)
address.grid(row=6, column=1, sticky="ew", padx=5)

buttons = [
    ("Add", add_record),
    ("View All", show_records),
    ("Search", search_record),
    ("Delete", delete_record),
    ("Clear", clear_fields),
    ("Save File", save_file),
    ("Load File", load_file)
]

button_frame = tk.Frame(root)
button_frame.grid(row=7, column=0, columnspan=4, pady=10)

for text, command in buttons:
    tk.Button(button_frame, text=text, command=command).pack(
        side="left", padx=4
    )

output = tk.Text(root, height=12, width=75)
output.grid(row=8, column=0, columnspan=4, padx=10, pady=10)

for col in range(4):
    root.grid_columnconfigure(col, weight=1)

root.mainloop()