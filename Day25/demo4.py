# Built-in scope is a special Python scope that’s created or loaded whenever you run a script or open an interactive session.
#  This scope contains names such as keywords, functions, exceptions, and other attributes that are built into Python.
#  Names in this Python scope are also available from everywhere in your code.
# It’s automatically loaded by Python when you run a program or script.


# LEGB - Rules

# Local rule : Firstly, it check within that self, if the value doesn't find within that self it will go
# up next scope
# Hierarchy - order - LEGB - Scope order of a variable (Local, Enclosed, Global, BuiltIn)

# def greet():
#     prod = 'Phone'
#     print(prod)
#
# greet()
# Phone

prod = 'Mobile'
def greet():
    print(prod)

greet()
# Mobile