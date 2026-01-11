# Cexm.py

class Cexm:
    def fsam(self):
        print("멤버 함수(메소드)")
    def fsbm(self, pa):
        self.x=pa
        print(f"맴버 변수 x는 {self.x}")

ca = Cexm()
ca.fsam()
ca.fsbm(10)