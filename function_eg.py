#ex:-1
def paint():
    print("painting")
paint()    

def add():
    a=20
    b =30
    c=a+b
    print(c)
add()

#ex:-2
def painter(msg):
    print("mesage",msg)
painter("paintng my house")

def even_odd(x):
    if (x % 2 == 0):
        print("it is a even number {}".format(x))
    else:
        print("it is odd number {}".format(x))
# i = int(input("enter checking a number even or odd : - "))        
even_odd(int(input("enter checking a number even or odd : - ")) )

def range_check(l,m):
    for j in range(l,m):
        print(j)


x=int(input())
y = int(input())        
range_check(x,y)

# fun return example:-
def checking_return():
    return "i am checking"  
data = checking_return()    
print(data)

# eg
s_username = "Kalai"
s_password = "Room"

def validate():
    name = input("enter username :- ")
    pass_w = input("enter a password :- ")
    if ((name  == s_username) & (pass_w == s_password)):
        print("Yes user name & Password is correct")
        return True
    else:
        return False
result = validate()    
print(result)
        

    
    
    