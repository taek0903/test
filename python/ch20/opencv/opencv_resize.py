# opencv_resize.py

import cv2

# 이미지 파일 읽기
image=cv2.imread(r"D:\rokey\python\ch20\opencv\rocket-8835386_640.png")

resized = cv2.resize(image,(300,300))


# 이미지 창에 표시
cv2.imshow('Load Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows