# Robust File Management and Directory Navigation Utility
import os
import sys

print("\n----------File Management Utility----------")

if len(sys.argv) > 1:
    log_file = sys.argv[1]
    print("Target log file: ", log_file)

    if os.path.isfile(log_file):
        print("\n-----Log file contents-----")
        with open(log_file, "r") as file:
            content = file.read()
            print(content)
    else:
        with open(log_file, "w") as file:
            file.write("Log file created successfully.\n")
            print("Log file not found. A new log file was created.")
else:
    print("No log file argument provided.")

print("\n-----Current location-----")
print(os.getcwd())

print("\n-----Directory Contents-----")
print(os.listdir())

directory = input("\nEnter directory to navigate to: ")
if os.path.isdir(directory):
    print("Directory found.")
    os.chdir(directory)
    print("Navigated to: ", os.getcwd())

    print("\n-----Workspace-----")
    workspace = input("Enter workspace folder name: ")
    if os.path.isdir(workspace):
        print("This workspace exists already.")
    else:
        os.mkdir(workspace)
        print("Workspace created successfully.")

    print("\n-----File extension search-----")
    extension = input("Enter file extension to search: ")
    files = []
    for filename in os.listdir():
        if filename.endswith(extension):
            files.append(filename)
    if files:
        print("\n---Matching Files---")
        for file in files:
            print(file)
    else:
        print("No matching files were found.")
else:
    print("Directory does not exist.")