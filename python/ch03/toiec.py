# toiec. py

tscore = 700
if tscore >= 900:
    print("당신의 토익점수는", tscore, "상위권 입니다.")
elif tscore >= 700:
# elif 900 > tscore >= 700 :
# 위 구문의 처리방식은 2번과 같다.(동시 평가: 내부적 처리)
# elif (900 > tscore) >= 700:
# 1번: True >=700       =>         1 >=700 : Fasle
# 2번: (900> tscore) and (tscore >= 700)
    print("당신의 토익점수는", tscore, "중위권 입니다.")
else:
    print("당신의 토익점수는", tscore, "하위권 입니다.")
print("if 문 종료됨")

print("------------------------------")
# 토익점수를 4분류 하는 프로그램
tscore = 200
if tscore >= 900:
    print("상위권 점수입니다.")
elif tscore >= 600:
    print("중상위권 점수입니다.")
elif tscore >= 300:
    print("중위권 점수입니다.")
else:
    print("하위권 점수입니다.")
print("if 문 종료")

print("------------------------------")
tscore = 250
if tscore >=900:
    print("상위권 점수입니다.")
if tscore < 900 and tscore >= 600:
    print("중상위권 점수입니다.")
if tscore < 600 and tscore >= 300:
    print("중위권 점수입니다.")
if tscore < 300:
    print("하위권 점수입니다.")
print("if 문 종료")