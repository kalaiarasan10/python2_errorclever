for i in "apple":
    print(i)
for i in range(0,5):
    print(i)

tables = int(input("what table u need:-  "))

for i in range (1,11):
    print("{} * {} = {}".format(tables,i,tables*i))

start = int(input("enter the start number:- "))
end = int(input("enter the end number:- "))
for i in range(start , end):
    if i%2 == 0:
        print("only even numbers",i)
