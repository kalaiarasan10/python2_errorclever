a = [1,2,3,4,5,6]
print(type(a))
a.append(7)
print(a)
a.insert(1,10)
a[0] = 30
print(a)
a.pop(5)
print(a)

# tuple 
b = (1,2,3,4)
c=list(b)
c[0]=23
print(b)
print(c)
k = tuple(c)
print(type(k))
print(type(c))
 
# set
h = {1,2,3,4,5}
h.add(10)
print(h)
print(type(h))

# dict
# d= {"name":"kalaiarasan","Age":"28","company":"LMW"}
d= ({"location":"chennai","mobile no:-" : "123456789"})
print(d.values())


 
 