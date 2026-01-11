# mex1_example.py
# 실행방법1:-m 모듈활용

#실행방법2 : sys 모듈활용
# import sys
# sys.path.append("D:/rokey")
# import python.ch09.Bag
# print('------------------')
# handBag = python.ch09.Bag.Bag("handBag")
# handBag.add("책")
# handBag.add("큐브")
# handBag.add("배터리")
# handBag.add("립밤")
# print(handBag.data)

print("실행방법3-------------")
#g하위 패키지 모듈 활용
import ch10_1.mex2
print(ch10_1.mex2.minus(10,5))