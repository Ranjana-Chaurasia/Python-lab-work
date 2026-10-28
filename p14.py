# Object Persistence Engine via Serialization
import pickle
import shelve

# Class representing an object
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Marks: {self.marks}")

s1 = Student("Riya", 101, 85)
s2 = Student("Aman", 102, 90)

# Save objects using pickle
with open("students.pkl", "wb") as file:
    pickle.dump([s1, s2], file)

print("Objects saved using pickle.")

# Restore objects using pickle
with open("students.pkl", "rb") as file:
    students = pickle.load(file)

print("\nRestored using pickle:")
for student in students:
    student.display()

# Save objects using shelve
with shelve.open("student_data") as database:
    database["student1"] = s1
    database["student2"] = s2

print("\nObjects saved using shelve.")

# Restore objects using shelve
with shelve.open("student_data") as database:
    print("\nRestored using shelve:")
    database["student1"].display()
    database["student2"].display()

print("\nObject persistence completed successfully.")