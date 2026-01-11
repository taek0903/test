# generator1.py

# 제너레이터 사용 예제
import time         # 시간 관련 모듈

def longtime_job():
    print("job start")
    time.sleep(1)   # 1초 지연
    return 'done'

list_job=(longtime_job() for i in range(5))
# print(list_job)
print(next(list_job))
print(next(list_job))
print(next(list_job))
print(next(list_job))
print(next(list_job))