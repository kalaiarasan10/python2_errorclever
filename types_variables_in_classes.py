class phone:
    charger_type = "c type" #class varaiable
    def __init__(self,m,n):
        self.brand = m # instance variable
        self.price = n
    def display(self):
        print("Brand:-",self.brand)
        print("Price:-",self.price)
        print("self:-",self.charger_type)


samsung = phone("samsung","10000")
redmi  = phone("redmi",23000) 
nokia = phone("nokia",11000)
samsung.display()
nokia.display()
redmi.display()
phone.charger_type = "A type"
samsung.display()
nokia.display()
redmi.display()
