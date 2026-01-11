# prac1.py

def fadd(a=1,b=2):
    total=0
    total = a+b
    return total

ohap=fadd(10,20)
print(f"ohp의 값은 {ohap}")
ohap2=fadd(10)
print(f"ohap2의 값은 {ohap2}")
ohap3=fadd()
print(f"ohap2의 값은 {ohap3}")
print('-----------------')

class Cadd:
    def fadd(self, a=1, b=2):
        self.x=a
        self.y=b
        self.hap=self.x+self.y
obj=Cadd()
obj.fadd(10,20)
print(f"객체 obj 내의 인스턴스 변수 hap의 값은 {obj.hap}")
obj.fadd(10)
print(f"객체 obj 내의 인스턴스 변수 hap의 값은 {obj.hap}")
obj.fadd()
print(f"객체 obj 내의 인스턴스 변수 hap의 값은 {obj.hap}")
print('-----------------')

class Animal:
    def __init__(self):
        self.name = "고양이"
    def sound(self):
        print("야옹")

cat=Animal()
print(cat.name)
cat.sound()
print('-----------------')

class Fruit:
    def __init__(self):
        self.name = "오렌지"
        self.color = "노란색"
    def taste(self):
        print("새콤하다.")

orange=Fruit()
print(orange.name,orange.color)
orange.taste()