# try_except2.py

# 파일 처리
# FileNotFoundError
# path="myfile.ext"
path=r"python\ch13\exception\myfile.text"
# open(path)            # mode 기본값 : 'r'
# f=open(path, 'w') 
# f = open(path,"r")      
# s = f.readline()
# i = int(s.strip())      # ValueError

try:
    # f=open('myfile.text')
    f=open(path)
    s=f.readline()
    # print(f"s: {s}")
    i=int(s.strip())
except OSError as err:                  # FileNotFoundError 처리 포함
    print('파일을 찾을 수 없습니다.')
    print(err)
except FileNotFoundError as err:  
    print('파일을 찾을 수 없습니다.')
    print(err)
except ValueError as err:
    print("정수형으로 변환할 수 없습니다.")
    print(err)
except Exception as err:
    print(f"Unexpected {err}, {type(err)}")
finally:
    print("예외처리여부와 관계없이 마지막 실행")
    f.close()
# finally 사용 이유 : 자원(Resource) 정리 보장
# 1. 파일 닫기
# 2. 네트워크 소켓 종료
# 3. Data Base연결 해제

print("program exit")