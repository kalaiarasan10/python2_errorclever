class goa:
    drink = "something"
    name = "Any thing"
    def party(self):
        print("Lets party......")
    def beach(self):
        print("enjoying beach")
ramesh = goa()
suresh = goa()

ramesh.party()
suresh.beach()

ramesh.name= "kalai"

print(ramesh.name)
print(suresh.name)

suresh.name = "suresh"
print(suresh.name)



#example 2

class laptop:
    price = ""
    processor = ""
    Ram =    ""
    
HP = laptop()
Lenovo = laptop()
Dell = laptop()

HP.price = int(input("Enter the price :- "))
HP.processor = input("Enter the Processor name:- ")
Dell.price = int(input("enter price"))
Lenovo.Ram = (int(input("enter ram :- ")))
print(HP.price )
print(HP.processor)
print(Dell.price)
print(Lenovo.Ram )
