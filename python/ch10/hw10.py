# hw10.py

# 5번
class Phone:
    def __init__(self, number, color):
        self.number=number
        self.color=color
phone=Phone("010-1234-5678","검정")
print(phone.number)
print(phone.color)
print('------------------------')

# 6번
class SmartPhone(Phone):
    def __init__(self, number, color, maker):
        super().__init__(number, color)
        self.maker=maker
print('------------------------')

# 7번
class SmartPhone(Phone):
    def __init__(self, number, color, maker):
        super().__init__(number, color)
        self.maker=maker

apple = SmartPhone("010-1234-5678","검정","애플")
print(apple.number)
print(apple.color)
print(apple.maker)
print('------------------------')

# 8번
class Phone:
    def __init__(self, number, color):
        self.number=number
        self.color=color
    def showinfo(self):
        print(f"전화번호: {self.number}")
        print(f"색상:{self.color}")
phone=Phone("010-1234-5678","검정")
phone.showinfo()
print('------------------------')

# 9번
# 10번
class SmartPhone(Phone):
    def __init__(self, number, color, maker):
        super().__init__(number, color)
        self.maker=maker
    def showinfo(self):
        super().showinfo()
        print(f"회사:{self.maker}")

apple = SmartPhone("010-1234-5678","검정","애플")
apple.showinfo()
print('------------------------')
