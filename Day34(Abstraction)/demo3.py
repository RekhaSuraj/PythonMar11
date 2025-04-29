#  Concrete Methods in Abstract Base Classes :
# Concrete classes contain only concrete (normal)methods whereas abstract classes may contain both concrete methods and abstract methods.
# The concrete class provides an implementation of abstract methods, the abstract base class can also provide an implementation by invoking the methods via super().

# Interface vs Abstract class Vs Concentrate class :
# 1.If we don't know anything about implementation, then just we have requirement specification then we should go for interface.(SRS, Service Requirement Specification)
#
# 2.If we are talking about implementation but not completely then we should go for abstract class (partially implementd class)
#
# 3.We are talk about implementation completely and ready to provide service then we should go for concrete class(Fully completed class).



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

    # concrete method
    def KYC(self):
        print('Verification - Know your customer')


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


class Profile:

    def perform_operation(self, bank_name:RBI):
        bank_name.CreateAccount()
        bank_name.Deposit()
        bank_name.WithDraw()
        bank_name.Loan()
        bank_name.KYC()


obj_Profile = Profile()
obj_Profile.perform_operation(HDFC())

# Submit documents
# Min Deposit amount is 1000Rs
# Min Withdraw amount is 500Rs
# Gold Loan price is 1lakh
# Verification - Know your customer
print()

obj_Profile.perform_operation(Canara())

# Submit documents with photo
# Min Deposit amount 500Rs
# Min Withdraw amount is 200Rs
# Home Loan interest rates start at 10%
# Verification - Know your customer

