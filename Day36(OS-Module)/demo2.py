import os

print(os.getcwd())
# F:\Rekha\GRKTrainings\PythonMar11\Day36(OS-Module)

# Create a directory
# os.mkdir("F:/Rekha/GRKTrainings/Demo/All Notes/os1-module")
# FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'F:/Rekha/GRKTrainings/Demo/All Notes/os1-module'

# To remove a directory
os.rmdir("F:/Rekha/GRKTrainings/Demo/All Notes/os1-module")

# If we try to run it again, we get the below error
# FileNotFoundError: [WinError 2] The system cannot find the file specified: 'F:/Rekha/GRKTrainings/Demo/All Notes/os1-module'
