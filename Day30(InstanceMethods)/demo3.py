class Bike:

    def __init__(self, Name, Model, Mileage, Price):
        self.name = Name
        self.model = Model
        self.mileage = Mileage
        self.price = Price


    def display(self):
        print("Name",self.name)
        print("Model",self.model)
        print("Mileage",self.mileage)
        print("Price",self.price)

    def delete_Model(self):
        del self.model


obj_Bike = Bike("Yamaha","BS6",40,10000)
obj_Bike.display()

# Name Yamaha
# Model BS6
# Mileage 40
# Price 10000
print()
obj_Bike.delete_Model()
obj_Bike.display()
# AttributeError: 'Bike' object has no attribute 'model'