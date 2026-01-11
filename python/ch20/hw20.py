# print('6-----------------')
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# data = np.random.normal(loc=50,scale=10,size=1000)

# sns.histplot(data,kde=True)
# plt.title("Histogram Example")
# plt.show()

# print('7-----------------')
# import seaborn as sns
# import matplotlib.pyplot as plt
# tips = sns.load_dataset("tips")
# sns.boxplot(data=tips,
#             x="day",
#             y="total_bill")
# plt.title("Tips Example")
# plt.show()

# print('8-----------------')
# import cv2

# image = cv2.imread(r'D:\rokey\python\ch20\opencv\family.jpg')

# cv2.imshow('Loaded Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print('9-----------------')
# import cv2
# image = cv2.imread(r'D:\rokey\python\ch20\opencv\woman.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imshow('Grayscale Image', gray)
# cv2.waitKey(0)
# cv2.imshow()

# print('10----------------')
# import cv2
# image = cv2.imread(r'D:\rokey\python\ch20\dog.jpg')
# edges = cv2.Canny(image,100,200)

# cv2.imshow('Canny Edge Detection',edges)
# cv2.waitKey(0)
# cv2.imshow()

class Counter:
    def __init__(self):
        self.n = 0
    def inc(self):
        self.n += 1
        return self.n
c = Counter()
a = c.inc()
b = c.inc()

print(b)
