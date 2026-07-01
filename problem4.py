import os

# Specify the directory path
path = "/"

# Get the list of files and directories
contents = os.listdir(path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)