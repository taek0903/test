# iterator.py

# 이터레이터 생성 방법2 : 직접 class 설계
class MyIterator:
    # 맴버 변수
    # 맴버 함수(메서드)
    def __init__(self,data):
        self.data = data
        self.position=0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result

if __name__ == "__main__":
    i = MyIterator([1,2,3])
    print(type(i))
    print(next(i))
    # print(i.__next__())
    print(f"위치: {i.position}")
    for item in i:
        print(item)
        print(f'위치: {i.position}')
    # print(next(i))          # StopIteration 