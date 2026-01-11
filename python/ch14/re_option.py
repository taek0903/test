# re_option.py
import re

# p = re.compile('a.b')
p = re.compile('a.b', re.DOTALL)
# p = re.compile('a/b', S)
m= p.match("a\nb")
print(m)

m = re.match('[a-z+.]', "python\n", re.DOTALL)
print(m)
print(m.group())

print('-----------------')
p = re.compile('[a-z]+', re.IGNORECASE)
# p = re.compile('[A-Z]+', re.IGNORECASE)
# p = re.compile('[a-z]+', re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))

print('-----------------')

# p = re.compile('^python\s\w+')
p = re.compile('^python\s\w+', re.MULTILINE)
# p = re.compile('^python\s\w+', re.M)

data ="""python one
life is too short
python two
you need python
python three"""
print(p.findall(data))

print('-----------------')
p=re.compile(r'&[#](0[0-7]+[0-9]+x[0-9a-fA-F]);')

p = re.compile(r"""
&[#]                                # 숫자형 엔티티(문자 개체 참조) 시작
(
               0[0-7]+              # Octal form(8진수 형식)
            [0-9]+              # Dcimal form(10진수 형식)
            x[0-9a-fA-F]+       # Hexadecimal form(16진수 형식)
)
;
""", re.VERBOSE)

data = "&#07; &#8; &#x0A;"          # 후행 semicolon

print(p.findall(data))