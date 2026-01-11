# score

score = 90
if score > 80:
    print("점수: ", score)
    print('합격입니다.')
print("-------------------")

score = 60
if score > 80:
    print("점수: ", score)
    print('합격입니다.')
else:
    print("점수: ", score)
    print('불합격입니다.')
print("-------------------")
# 짝수 확인
na=21
na=20
if na % 2==0:
    print(na, "짝수")
print("if 문 종료 됨")
print("-------------------")
# 홀/짝수 확인
na=21
if na % 2==0:
    print(na, "짝수")
else:
    print(na, "홀수")
print("if 문 종료 됨")

print("-------------------")
tscore = 700
if tscore > 900:
    print("당신의 토익 점수는", tscore, "상위권 점수입니다.")
elif tscore > 700:
    print("당신의 토익 점수는", tscore, "중위권 점수입니다.")
else :
    print("당신의 토익 점수는", tscore, "하위권 점수입니다.")
print("if 문 종료됨")