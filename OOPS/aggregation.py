class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    
    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name = new_name
        self.address.change_address(new_city,new_pin,new_state)
        print(self.name,self.address.city,self.address.pincode,self.address.state)

class Address:
    def __init__(self,city,pincode,state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_address(self,new_city,new_pin,new_state):
        self.city = new_city
        self.pincode = new_pin
        self.state = new_state

address_1 = Address("Jabalpur",482001,"Madhya Pradesh")
customer_1 = Customer("Name","Male",address_1)
customer_1.edit_profile("Name_1","Jabalpur_1",482001,"Madhya_Pradesh")