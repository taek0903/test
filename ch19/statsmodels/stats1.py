# stats1.py

import statsmodels.api as sm

# 데이터 가져오기
data = sm.datasets.get_rdataset("mtcars").data
print(data)
print(type(data))

X = data['hp']      # 마력
y = data['mpg']     # 연비

# 상수항 추가
X=sm.add_constant(X)

# 모델 생성 및 학습
# - 알고리즘 선택
# - 모델 학습 => 그래프 찾기!
# ols = sm.OLS(y,X)
# model = ols.fit()
model = sm.OLS(y,X).fit()

print(model.summary())

print('모델 계수--------------')
print(model.params[1])      # 기울기
print(model.params[0])      # 절편

