# xor-train2.py
# D:\rokey\python\ch19\sklearn\xor\xor.py

from sklearn import svm
from sklearn import metrics
import pandas as pd

xor_data = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
]
xor_df = pd.DataFrame(xor_data)

data = xor_df.loc[:, 0:1]
label = xor_df.loc[:, 2]

clf =svm.SVC()      # 알고리즘 tjsxor
# fit(학습데이터, 학습레이블)

clf.fit(data,label)

# 데이터 예측하기
# predict(테스트데이터)
pre=clf.predict(data)      # 예측 => 답
print(f'예측결과: {pre}')

# 결과 확인
ac_score = metrics.accuracy_score(label, pre)
print(f'정답률: {ac_score}')