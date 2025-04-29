# What is an abstract class in Python?
# What is an interface in Python?
# Difference between abstract class and interface in Python
#
# What is an Abstract class in Python?
# A blueprint for other classes might be thought of as an abstract class. You may use it to define a collection of methods
#
#
# 1.what is the advantage of declaring abstract methods in Parent class ?
# a).By declaring abstract methods in parent class we provide guidelines to the child classes,
#  such that which methods compulsory they should implement.
#
# 2. Is a class can contain both abstract and non-abstract methods ?
# a).yes
# Note : if a class contains both abstract and non-abstract methods then child class is responsible to provide implementation only for abstract methods.
#
# The Most Important Conclusion :
# 1.If a class contains at least one abstract method and if we are extending ABC class then instantiation is not possible.
# " For Abstract class with abstract methods, instantiation is not possible ".



from abc import ABC,abstractmethod
class RBI(ABC):
    @abstractmethod
    def CreateAccount(self):
        pass

    @abstractmethod
    def Deposit(self):
        pass

    @abstractmethod
    def WithDraw(self):
        pass

    @abstractmethod
    def Loan(self):
        pass

class HDFC(RBI):

    def CreateAccount(self):
        print('Submit documents')


    def Deposit(self):
        print('Min Deposit amount is 1000Rs')


    def WithDraw(self):
        print('Min Withdraw amount is 500Rs')


    def Loan(self):
        print('Gold Loan price is 1lakh')


class Canara(RBI):

    def CreateAccount(self):
        print('Submit documents with photo')


    def Deposit(self):
        print('Min Deposit amount 500Rs')


    def WithDraw(self):
        print('Min Withdraw amount is 200Rs')


    def Loan(self):
        print('Home Loan interest rates start at 10%')


obj_HDFC = HDFC()
obj_HDFC.CreateAccount()
obj_HDFC.Deposit()
obj_HDFC.WithDraw()
obj_HDFC.Loan()

print()
obj_Canara = Canara()
obj_Canara.CreateAccount()
obj_Canara.Deposit()
obj_Canara.WithDraw()
obj_Canara.Loan()

# Submit documents
# Min Deposit amount is 1000Rs
# Min Withdraw amount is 500Rs
# Gold Loan price is 1lakh
#
# Submit documents with photo
# Min Deposit amount 500Rs
# Min Withdraw amount is 200Rs
# Home Loan interest rates start at 10%