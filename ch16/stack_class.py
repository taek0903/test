# stack_class.py
class Stack:
    def __init__(self):
        self.stack =[]
    
    # 1. push
    # 기능 : 스택에 데이터 넣기
    # 입력 : 데이터
    # 반환 : 없음
    def push(self, data):
        self.stack.append(data)
    
    # 2. pop
    def pop(self):
        # 3. 비어있는 경우 고려
        if not self.is_empty():
            return self.stack.pop()
        return

    # 4. 스택 내 데이터 유무 확인
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    # 5. 스택 최상위(top) 데이터 확인
    #   - 스텍 내 데이터 유무 확인
    def peak(self):
        if not self.is_empty():
            return self.stack[-1]
        return

    # 6. 스택 상태 반환
    def statu_stack(self):
        return self.stack

if __name__=="__main__":
    s1 = Stack()
    print(s1.peak())
    s1.pop()
    s1.push(1)
    s1.push(2)
    s1.pop()
    s1.push(3)
    s1.push(4)
    print(s1.peak())
    print(s1.statu_stack())

# 소프트웨어 공학
# 고객: 제안요청서(세부사항x)
# 기업
# 0. 아이디어 회의
# 1. 제안서(기술, 큰그림, 일정, 상품)
# 2. 요구명세서
#  - 사용자 요구사항 정리
#  - 프로그램 기능 정의
#  - 기능 모델링
#  - 화면(인터페이스) 설계
# 3. 설계명세서
#  - 어떻게 구현?
#  - 데이터 모델링(데이터 베이스)
#  - 서비스(프로그램) 구조
#  - 프로토타입 정의
# 4. 구현 명세서
#  - 구체적인 클래스, 함수 구현(데이터 활용)
#  - 클래스 다이어그램
# 5. 개발(구현)
#   - 프로그램 작성
# 6. 테스트
# 7. 베포
# 8. 유지보수
