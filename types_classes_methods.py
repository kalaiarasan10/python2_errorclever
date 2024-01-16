class laptop:
    charger_type = "c type"
    def __init__(self):
        self.brand = ""
        self.price = 34
    def set_price(self,price):
        self.price = price
    def get_price(self):
        print(self.price)


    @classmethod
    def changecharger_type(cls):
        cls.changecharger_type = "B type"
        print("charger type chnaged to b",cls.changecharger_type)
    @staticmethod
    def info():
        print("This is laptop class")
    
hp = laptop()
hp.get_price()
hp.set_price(20000)
hp.get_price()
laptop.changecharger_type()
hp.info()

