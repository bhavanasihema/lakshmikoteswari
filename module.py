import os

folder = input("Enter folder name: ")
filename = input("Enter file name: ")

# Check if folder exists
if not os.path.exists(folder):
    os.mkdir(folder)
    print("Folder created")

# Create file inside the folder
path = os.path.join(folder, filename)

file = open(path, "w")
file.write("File created successfully")
file.close()

print("File created at:", path)