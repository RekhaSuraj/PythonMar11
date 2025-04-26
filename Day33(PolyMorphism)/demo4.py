class College:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    # __str__ overrdiding
    def __str__(self):
        return f'{self.x},{self.y}'

    # + operator overriding
    def __add__(self, other):
        return f'{self.x+other.x},{self.y+other.y}'



obj_College = College(5,7)
print(obj_College)
# 5,7

obj_College1 = College(10,2)
print(obj_College1)
# 10,2

print(obj_College + obj_College1)

# This tells Python how to behave when you write obj1 + obj2.
# Instead of the default behavior (which would raise an error), it adds the a and b values from both objects and returns a formatted string.

# Calls __add__:
# self.a = 5, self.b = 7
# other.a = 10, other.b = 2
# Result: 5+10 = 15, 7+2 = 9
# Returns: '15,9'



