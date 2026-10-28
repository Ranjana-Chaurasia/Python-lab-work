# Modular Multi-Frame Graphical Dashboard Application
import tkinter as tk
from tkinter import messagebox
import json
import os

FILE = "dashboard_config.json"

# Model: Stores application data
class DashboardModel:
    def __init__(self):
        self.config = {"username": "", "theme": "Light"}

    def save(self):
        with open(FILE, "w") as f:
            json.dump(self.config, f, indent=4)

    def load(self):
        if os.path.exists(FILE):
            with open(FILE, "r") as f:
                self.config = json.load(f)

# Main application
class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Frame Dashboard")
        self.geometry("600x400")
        self.model = DashboardModel()
        self.model.load()

        menu = tk.Menu(self)
        pages = tk.Menu(menu, tearoff=0)
        pages.add_command(label="Home", command=lambda: self.show("Home"))
        pages.add_command(label="Settings", command=lambda: self.show("Settings"))
        pages.add_command(label="About", command=lambda: self.show("About"))
        menu.add_cascade(label="Pages", menu=pages)
        menu.add_command(label="Save", command=self.save)
        menu.add_command(label="Exit", command=self.quit)
        self.config(menu=menu)

        # Container for screens
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}
        for Page in (HomePage, SettingsPage, AboutPage):
            frame = Page(container, self)
            self.frames[Page.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show("Home")

    def show(self, page):
        name = page + "Page"
        self.frames[name].tkraise()

    def save(self):
        try:
            self.model.save()
            messagebox.showinfo("Saved", "Dashboard settings saved!")
        except OSError:
            messagebox.showerror("Error", "Unable to save settings.")

# Home screen
class HomePage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        tk.Label(self, text="Welcome to Dashboard",
                 font=("Arial", 20)).pack(pady=20)

        tk.Label(self, text="Enter your name:").pack()
        self.name = tk.Entry(self)
        self.name.pack(pady=5)

        tk.Button(self, text="Submit",
                  command=lambda: self.submit(app)).pack(pady=5)

    def submit(self, app):
        name = self.name.get().strip()
        if not name:
            messagebox.showwarning("Warning", "Please enter your name.")
            return

        app.model.config["username"] = name
        messagebox.showinfo("Welcome", f"Hello, {name}!")

# Settings screen
class SettingsPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        tk.Label(self, text="Settings",
                 font=("Arial", 20)).pack(pady=20)

        self.theme = tk.StringVar(value=app.model.config["theme"])
        tk.Label(self, text="Choose Theme:").pack()

        for value in ("Light", "Dark"):
            tk.Radiobutton(self, text=value, variable=self.theme,
                           value=value).pack()

        tk.Button(self, text="Apply Settings",
                  command=lambda: self.apply(app)).pack(pady=10)

    def apply(self, app):
        app.model.config["theme"] = self.theme.get()
        messagebox.showinfo("Settings", "Theme preference updated!")

# About screen
class AboutPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        tk.Label(self, text="About This Application",
                 font=("Arial", 18)).pack(pady=30)
        tk.Label(self, text="A modular dashboard built using Python Tkinter."
                 ).pack(pady=10)

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()