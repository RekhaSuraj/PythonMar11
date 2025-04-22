class Car:

    car_Name = "Fortuner"
    car_Color = "White"
    car_Price = 5000000
    car_Type = "Petrol"


car_obj = Car()
# Fetch values
print(car_obj.car_Name)
print(car_obj.car_Color)
print(car_obj.car_Price)
print(car_obj.car_Type)

# Fortuner
# White
# 5000000
# Petrol

# update these values
car_obj.car_Color = "Black"
car_obj.car_Type = "Diesel"

print()
# After updating the values
print(car_obj.car_Name)
print(car_obj.car_Color)
print(car_obj.car_Price)
print(car_obj.car_Type)

# Fortuner
# Black
# 5000000
# Diesel

print()
# Delete car_Price attribute of car object
del car_obj.car_Price

print(car_obj.car_Name)
print(car_obj.car_Color)
print(car_obj.car_Price)
print(car_obj.car_Type)

# If we try to access an attribute once deleted, we get this error
# AttributeError: 'Car' object has no attribute 'car_Price'Fortuner


