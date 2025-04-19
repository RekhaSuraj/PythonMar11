import sys

# Set a user defined recursion limit
sys.setrecursionlimit(100)

def Call():
    print('Welcome')
    Call()

Call()
#   [Previous line repeated 96 more times]
# RecursionError: maximum recursion depth exceeded