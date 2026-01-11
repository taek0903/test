# hw_p9.py

# 9. 고정된 크기의 원형 큐를 구현하세요. (다음 내용을 고려할 것.)
# enqueue(x): 정수 x를 큐의 끝에 추가. (큐가 가득 차면 추가하지 않음)
# dequeue(): 큐의 앞에서 값을 제거하고 반환. (큐가 비어 있다면 -1 반환)
# front(): 큐의 앞에 있는 값을 반환. (비어 있다면 -1 반환)
# is_empty(): 큐가 비어 있으면 True, 아니면 False 반환
# is_full(): 큐가 가득 차 있으면 True, 아니면 False 반환

# 특징
# 배열의 마지막 인덱스 다음에 다시 첫번째 인덱스로 연결되는 구조
# 끝에 도달하면 다시 처음(0)으로 돌아가라
# rear = (rear +1)% size

# 장점 : 선형 큐 앞쪽 데이터 삭제시, 
# 빈 공간의 재사용을 위해 데이터를 앞으로 당겨야 함

class CircluarQueue:
    def __init__(self,size):
        # 고정 크기 배열 생성, 아직 데이터가 없으므로 전부 None
        self.queue = [None]*size
        # empty / full 판단 기준
        self.count = 0      # 저장된 데이터 수
        self.front_idx=0        # 다음에 꺼낼 위치
        self.rear_idx=0         # 다음에 넣을 위치(아직 비어있는 칸)
        self.size = size

    def enqueue(self,x):
        if self.is_full():      # 큐가 가득차면 종료
            return
        # rear_idx 위치에 값 저장
        self.queue[self.rear_idx] = x
        self.rear_idx = (self.rear_idx +1)% self.size
        self.count+=1
    
    def dequeue(self):
        if self.is_empty():   # 큐가 비어있으면
            return -1
        # front 위치 값 저장 : 실제 제거될 데이터
        value = self.queue[self.front_idx]
        # 시각적/논리적 삭제
        self.queue[self.front_idx] = None
        # front 인덱스 원형 이동 : 다음에 꺼낼 위치 이동
        self.front_idx = (self.front_idx +1)% self.size
        self.count -= 1
        return value 
    
    def front(self):
        if self.is_empty():
            return -1
        return self.queue[self.front_idx]
        
    def is_empty(self):
        return self.count==0
    
    def is_full(self):
        return self.count==self.size
    
cq = CircluarQueue(3)
print(cq.queue)
print(cq.is_empty)

cq.enqueue(10)
print(cq.queue)
cq.enqueue(20)
print(cq.queue)
cq.enqueue(30)
print(cq.queue)

cq.enqueue(40)
print(cq.queue)

print(cq.front())
print(cq.dequeue())
print(cq.queue)
print(cq.is_full())

cq.enqueue(40)
print(cq.queue)