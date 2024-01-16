class a():
    def __init__(self):
        print("A")
    def displa():
        print("just display")
class b():
    def __init__(self):
        super().__init__()
        print("B")
    def displa():
        print("just display")
class C(b,a):
    def __init__(self):
        super().__init__()
        print("c")
    def displa():
        print("just display")

ob1 = C()