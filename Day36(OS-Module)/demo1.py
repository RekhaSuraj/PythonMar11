import os

# os.getcwd() - Return a unicode string representing the current working directory
print(os.getcwd())
# F:\Rekha\GRKTrainings\PythonMar11\Day36(OS-Module)

# To change directory
# os.chdir("F:\\Rekha\\GRKTrainings\\Demo\\All Notes")
# SyntaxWarning: invalid escape sequence '\R'
# or
os.chdir("F:/Rekha/GRKTrainings/Demo/All Notes")

print(os.getcwd())
# F:\Rekha\GRKTrainings\Demo\All Notes

# To list all files inside my working directory
# os.listdir() - Return a list containing the names of the files in the directory.
print(os.listdir('F:/Rekha/GRKTrainings/Demo/All Notes'))
# ['AbstractInterfaceDiff.png', 'abstraction.txt', 'chain multiple if statement in Pyt.txt', 'class methods.txt', 'Class Variable.txt', 'constructors.txt', 'control flow statements.txt', 'Day1 -Python and Variables.txt', 'Day2 -Type conversion or casting.txt', 'Day3 -Operators.txt', 'Day4 - Operators Contd.txt', 'Dictionary.txt', 'Django Notes.docx', 'Encapsulation.png', 'example.txt', 'FileHandling.txt', 'Find first and second largest numbe.txt', 'Flow control statements.txt', 'for loop programs.txt', 'Fulllambda.txt', 'Functions.txt', 'hex table.docx', 'Inheritance.txt', 'Instance vs class vs static methods.jpeg', 'Interface vs Abstract class Vs Conc.txt', 'Keybindings.txt', 'Keywords and Rules.txt', 'lambda contd.txt', 'list.txt', 'map filter contd.txt', 'nested for loop.txt', 'Nested functions.txt', 'OOPS.txt', 'OS Module.txt', 'polymorphism.png', 'Polymorphism.txt', 'PracticeNotes.txt', 'prime number check.txt', 'Programs on HOF.txt', 'PVM.png', 'PythonDatatypes.docx', 'RekhapracticeMySQL.txt', 'Scope of Variables.txt', 'set.txt', 'simple programs.txt', 'Slicing.txt', 'staticmethods and inheritance.txt', 'String difference between find() an.txt', 'String Programs.txt', 'time module.txt', 'tuple.txt', 'user input.txt', 'user modules.txt', 'Variable-Length Arguments in Python.txt', 'While loop.txt']


# To get the number of files
print(len(os.listdir()))
# 55