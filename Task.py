import os
import shutil

source_folder = input("Enter source folder path: ")
destination_folder = input("Enter destination folder path: ")

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

count = 0

for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        shutil.move(
            os.path.join(source_folder, file),
            os.path.join(destination_folder, file)
        )
        count += 1

print(f"\n{count} JPG file(s) moved successfully!")
