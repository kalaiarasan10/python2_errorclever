# mark = int(input("Enter the mark"))
# if(mark >= 35):
#     print("Pass")
# else:
#     print("Fail")

# #example 2
    
# a = int(input("Enter the number both divisble 3 & 5 :-  "))

# if (a%3 == 0 and a%5 == 0):
#     print("both number are divisible 3& 5")
#     print(a)
# else:
#     print("no")
    
#example 3 nested loop

for i in range (1,5):
    print("week: {}".format(i))
    for j in range (1,8):
        print("day : {} ".format(j))

# example program * 4

for i in range (1,9):
    for j in range (0,i):
        print("{}".format(i),end="|")
    print()