class User:
    def login(self):
        print("login")
    
    def register(self):
        print("register")

class Student(User):
    def enroll(self):
        print("Enroll")
    
    def get_details(self):
        print("Details")
    
    def register(self):
        super().register() # this will call register function of parent class