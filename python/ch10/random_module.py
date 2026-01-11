# rando,_module.py

import random
animals = ['체셔고양이','오리','도도새']
print(random.choice(animals))
print(random.choice(animals))

print('-------------------------')
print(random.sample(animals,2))
print(random.sample(animals,2))

print('-------------------------')
print(random.randint(1,100))
print(random.randint(1,100))

lottery = range(1,45)
for i in range(0,4):
    print(random.sample(lottery,6))