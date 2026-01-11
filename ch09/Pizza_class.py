# Pizza_class.py

# # 클래스 정의
# class 클래스명:
#     # 맴버면수
#     변수명 = 데이터값

#     # 맴버함수(매서드)
#     def 함수명(self, 매개변수1, ....):
#         코드블록
#         self.변수명 = 데이터값
#         return 반환값

# # 객체 생성(생성자함수 사용)
# 객체명 = 클래스명(인수)

# # 객체 접근
# 객체명.변수명
# 객체명.함수명(인수1, ...)

class Pizzaclass:
    def order(self):
        print("주문하다.")
        self.kind=10 # 함수내의 지역변수

combo = Pizzaclass()
potato = Pizzaclass()

combo.order()
print(combo.kind)

potato.order()
print(potato.kind)

class Singer:
    name = "아이유"
    def sing(self):
        print("이 밤 그날의 반딧불을 당신의 창 가까이 보낼게요~")
iu = Singer()
print(iu.name)
iu.sing()