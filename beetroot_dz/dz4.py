import random
number=random.randint(1,10)
while True:
    answer = input('Please enter lucky number :')
    try:
        answer = int(answer)
    # Поймаем просто все исключения
    except Exception:
        print('Not digit answer')
        continue
    if answer==number:
        print('Yes you like the number was {0}'.format(number))
        break
    else:
        continue

#Задача2
name=input('Please enter your name :')
age=input('Please enter your age :')
try:
    age=int(age)
except Exception:
    print('No digit age')
print('Your name is',name,'yor next birthday',age+1)