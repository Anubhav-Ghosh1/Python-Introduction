class Car:
    def __init__(self,price,brand):
        self.brand = brand
        self.price = price
    def print_value(self):
        print(self.brand)

car1 = Car(1000,"Audi")
car1.print_value()




class ATM:
    def __init__(self): # __init__ is the constructor
        self.pin = ""
        self.balance = 1000000
        print("Self ",self)
        self.menu()

    def menu(self):
        while True:
            user_input = int(input("""
        Welcome to the ATM
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit """))

            if user_input == 1:
                self.create_pin()
            elif user_input == 2:
                self.deposit_amount()
            elif user_input == 3:
                self.withdraw_amount()
            elif user_input == 4:
                print(self.get_balance())
            else:
                return None

    def create_pin(self):
        self.pin = int(input("Enter your pin "))
        print("Pin is successfully updated")

    def deposit_amount(self):
        value = int(input("Enter amount: "))
        self.balance += value
    
    def withdraw_amount(self):
        temp_pin = int(input("Enter pin "))
        if temp_pin != self.pin:
            return None
        
        value = int(input("Enter amount "))
        if self.balance < value:
            print("Insufficient balance")
            return None
        self.balance -= value
    
    def get_balance(self):
        return self.balance
    
class Fraction:
    def __init__(self,n,d):
        self.n = n
        self.d = d
    def __str__(self): # Automatically called when print is used
        return "{}/{}".format(self.n,self.d)
    def __add__(self,second_self):
        updated_d = self.d * second_self.d
        updated_n = (self.n*second_self.d) + (self.d * second_self.n)
        return "{}/{}".format(updated_n,updated_d)
    
fraction_1 = Fraction(2,5)
fraction_2 = Fraction(2,5)
value = fraction_2 + fraction_1
print(value)

# Instance variable
# varaibles inside constructor is called as instance variable

# Encalsulation
class Encapsulation:
    def __init__(self):
        self.__value = "" # __ marks value as private
    
    def __get_value(self):
        return self.__value
    
    def get_pin(self):
        return self.__value
    def set_pin(self,value):
        if type(value) != int:
            return None
        self.__value = value

Encapsulation_1 = Encapsulation()

# Pass by reference
class Customer: 
    def __init__(self,name):
        self.name = name

def greet(customer):
    print(customer.name)

customer_1 = Customer("Name")
greet(customer_1)