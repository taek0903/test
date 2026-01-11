# mex1_example.py
# import mex1 # 모듈 불러오기
from mex1 import Cvalue
from mex1 import plus
from mex1 import p1

from mex1 import *

# 클래스 활용
p2=Cvalue()
p2.fprint()
print(p2.lista)

# 함수 활용
value=plus(10,20)
print(value)

# 변수 활용
print(p1.lista)
p1.add(4)
p1.fprint()
