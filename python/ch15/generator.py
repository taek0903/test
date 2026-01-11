# generator.py

def simple_generator():
    yield 'a'
    yield 'b'
    yield 'c'

g = simple_generator()
print(type(g))

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))      # StopIteration

for item in g:
    print(item)

print("------------------")
# dir() : 객체의 속성을 보여주는 함수
print(dir(g))
print('__iter__' in dir(g))
print('__next__' in dir(g))

# 제너레이터는 이터레이터의 한 종류

print("------------------")

def mygen():
    for i in range(1,100):
        result = i*i
        yield result

gen = mygen()
print(next(gen))
print(next(gen))
print(next(gen))
for item in gen:
    print(item)