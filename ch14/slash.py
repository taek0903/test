# slash.py

import re

# p = re.compile('\section')
# p = re.compile('\\section')
p = re.compile('\\\\section')
p = re.compile(r'\\section')

m = p.match('\section')
print(m)

# 목적 : \section

# 1. \s 화이트스페이스
# \\section

# 2. 파이썬 리터럴 규칙(이스케이프)
# "\\" => "\"
# "\\\\" => "\\"

# raw string
# 파이썬 문자열 리터럴 안에서
# "이스케이프 코드처리를 없애주는 역할"