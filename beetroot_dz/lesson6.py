#Итак для вывода индексов и элементов массива применяется функция enumerate индексы начинаются с нуля как мы помним
countries=['Ukrain','Belarus','Germany','France','Serbia',
           'Finland']

for i,countrie in enumerate(countries):
    print(countrie,i+1)

positions=[1,2,3]
#Если применяем функцию zip то будет как бы два кортежа
new=zip(positions,countries)
print(new)
print('---------------------------------')
for i,countrie in zip(countries,positions):
    print(i,countrie)

sevens=[]
for i in range(1,71):
    if i%7==0:
        sevens.append(i)
print(sevens)
#Также можно и по другому от нуля с шагом 7
sevens=[]
for i in range(0,71,7):
    sevens.append(i)
print(sevens)

print('-------------------')
#То же самое только с вайл цикло
sevens=[]
i=0
while i<=70:
    sevens.append(i)
    i+=7
print(sevens)

import random
points=0
while True:
    x=random.randint(0,10)
    y=random.randint(0,10)
    print('points : '+str(points))
    answer=input(str(x)+'+'+str(y)+'=? [or press  q to exit] :')
    if answer=='q':
        break
    elif int(answer)!=x+y:
        print('No points for you!')
        continue
    print('Good job')
    points+=1