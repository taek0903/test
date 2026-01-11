# rev_interator.py

class ReverseIterator:
    def __init__(self,data):
        self.data=data
        self.position = len(self.data)-1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position < 0:
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result

ri = ReverseIterator([1,2,3,4,5,6])
print(next(ri))
print(next(ri))

if __name__ == "__main__":
    i = ReverseIterator([1,2,3])
    for item in i:
        print(item)

# 변수명, 함수명, 클래스명 이름 작성시 활용법
# 단어와 단어 구분 방법
# 1. 대문자 => 카멜 케이스 : 클래스 (함수)
# ex) ReverseIterator
# 2. 언더바(_) => 스네이크 케이스 : 변수
# ex) reverse_iterator

# 변수명 => [타입]+명사 : i_Num, f_Array, bType
# 함수명 => 동사+명사 : check_list, checklist
# 상수명 => 대문자 : PI