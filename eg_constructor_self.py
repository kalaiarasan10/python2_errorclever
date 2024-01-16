class student:
    def __init__(self):
        self.Name = ""
        self.roll_no = ""
    def display(self):
        print("Name:-",self.Name)
        print("Roll no :- ",self.roll_no)
s1 = student()
s2 = student()

s1.Name = "kalaiarasan"
s1.roll_no = "25"

s2.Name = "damo"
s2.roll_no = "28"

s1.display()
s2.display()


#exampl 2
# assigning a variable
class Fruit:
    def __init__(self):
        color = ""
        
apple = Fruit()
apple.color = "Red"
print("Apple color = ",apple.color)

#example 3
# variable passing through a parameter

class Fruits:
    def __init__ (self,x):
        self.colour = x



banana = Fruits("green")
print("colour of banana = ",banana.colour)




#example 4

class Teacher:
    def __init__ (self,x,y):
        self.name = x
        self.register = y
    def display(self):
        print("name :- ",self.name)
        print("register no:- ", self.register)
        
t1 = Teacher("malar","1234")
t2 = Teacher("nivi","3333")

# t1.name = "malar"
# t1.register = "1234"

# t2.name = "nivi"
# t2.register = "33"

t1.display()
t2.display()


#eg 4:-
class calculator:
    def __init__(self,g,h):
        self.a = g
        self.b = h
    def Add (self):
        print("Addition :- ",self.a+self.b)
    def sub (self):
        print("sub :- ",self.a-self.b)
    def mul (self):
        print("multi :- ",self.a*self.b)
    def div (self):
        print("Divi :- ",self.a/self.b)

math = calculator(25,35)



math.Add()
math.sub()
math.div()
math.mul()














