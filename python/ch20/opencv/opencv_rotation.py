# opencv_rotation.py

import cv2

# 이미지 파일 읽기
image=cv2.imread(r"D:\rokey\python\ch20\opencv\rocket-8835386_640.png")

(h,w) = image.shape[:2]
print(f'높이:{h}')
print(f'너비:{w}')
center = (w//2,h//2)

M = cv2.getRotationMatrix2D(center,45,1.0)
rotated = cv2.warpAffine(image,M, (w,h))

# 이미지 창에 표시
cv2.imshow('Grayscale Image', rotated)
cv2.waitKey(0)              # 0: 무한대긴, 대기 시간(ms)
cv2.destroyAllWindows       # 모든 OpenCY 창 닫기