# hw09.py

# 3번 4번
class Phone:
    pass

my_phone = Phone()
print('---------------------------------------------')
# 5번
class Phone:
    def __init__(self):
        print("휴대폰 생성")

my_phone = Phone()
print('---------------------------------------------')
# 6번 7번
class Phone:
    def __init__(self, maker, year, color):
        self.maker=maker
        self.year=year
        self.color=color
        print("제조사:", maker,"출고년도:", year, "색상:", color)

my_phone = Phone("samsung",2025, "red")
print('---------------------------------------------')
# 8번
class Phone:
    def __init__(self, maker, year, color):
        self.maker=maker
        self.year=year
        self.color=color
    def info(self):
        print("제조사:",self.maker,"출고년도:",self.year,"색상:",self.color)

my_phone=Phone("samsung",2025,"black")
my_phone.info()
print('---------------------------------------------')
# 9번
class Phone:
    def __init__(self, maker, year, color):
        self.maker=maker
        self.year=year
        self.color=color
    def setinfo(self, maker, year, color):
        self.maker=maker
        self.year=year
        self.color=color
    def info(self):
        print(f"제조사:{self.maker}, 제조년도:{self.year}, 색상:{self.color}")

my_phone=Phone("samsung",2025,"black")
my_phone.info()
my_phone.setinfo("apple",2025,"white")
my_phone.info()
print('---------------------------------------------')