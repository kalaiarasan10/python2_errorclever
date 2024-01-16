# class dad():
#     def phone(self):
#         print("dad's phone")
# class mom(dad):
#     def sweet(self):
#         print("Mom sweet")
# class son(mom):
#     def laptop(self):
#         print("This is sons laptop")

# ram = son()
# ram.laptop()
# ram.sweet()
# ram.phone()

#example 2

class dad():
    def money(self):
        print("dad money")
class land():
    def important(self):
        print("important land")
class son1(dad,land):
    pass
class son2(dad):
    pass
class son3(dad):
    pass

s1 = son1()
s1.money()

s2 = son2()
s2.money()

s3 = son3()
s3.money()

s1.important()
s2.important()



