class Cars():
    def __init__(self):
        self.price = 100000

    def getTotalCost(self):
        return self.price * 1.06

    def member_or_not(self):
        return False

class Ferrari(Cars):
    pass

class Audi(Cars):
    def member_or_not(self):
        return True

class R8(Audi):
    def __init__(self):
        self.price = 170000

class A8(Audi):
    pass

audi1 = Ferrari()
print(audi1.member_or_not())