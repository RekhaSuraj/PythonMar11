# overriding inbuilt methods
# '', print(), f'{}
# So __str__ is called in print(),str() and format(). So here let us override it and see from print() method

class College:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    # Overridding __str__ method
    def __str__(self):
        return f'Hello Students {self.x},{self.y}'


ob1 = College("Swaroop","Surendra")
print(ob1)
# Hello Students Swaroop,Surendra