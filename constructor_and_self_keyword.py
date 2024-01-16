class laptop:
    def __init__(self):
        self.ram = ""
        self.processor = ""
    def display(self):
        print("ram:",self.ram)
        print("processor:",self.processor)

hp = laptop()
dell = laptop()

dell.ram = "16gb"
dell.processor = "i7"

hp.ram = "8gb"
hp.processor = "i5"

hp.display()
dell.display()