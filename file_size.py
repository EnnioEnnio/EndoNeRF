import os
import math


def get_folder_size(folder_path):
    total_size = 0
    for path, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(path, file)
            total_size += os.path.getsize(file_path)
    return total_size


# Provide the path to your folder
folder_path = "/dhc/home/ennio.strohauer/EndoNeRF/logs"

# Call the function to get the folder size
size_in_bytes = get_folder_size(folder_path)

# Convert the size to a human-readable format


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_names = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    size = round(size_bytes / math.pow(1024, i), 2)
    return f"{size} {size_names[i]}"


size_in_human_readable = convert_size(size_in_bytes)
print(f"The size of the folder is: {size_in_human_readable}")
