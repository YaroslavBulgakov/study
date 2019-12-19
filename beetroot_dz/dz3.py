#Задача 2
result=100/10
while True:
    answer=input('Please 100/10 enter the answer :')
    try:
        answer=int(answer)
    except Exception:
        print('Not digit answer')
        continue
    if type(answer) is int and answer==result:
        print('Your answer is OK')
        break
    else:
        print('Yor answer is WRONG')
        continue

#Задача 2
result=100/10
while True:
    answer=input('Please 100/10 enter the answer :')
    try:
        answer=int(answer)
    #Поймаем просто все исключения
    except Exception:
        print('Not digit answer')
        continue
    if type(answer) is int and answer==result:
        print('Your answer is OK')
        break
    else:
        print('Yor answer is WRONG')
        continue
#Задача 1 валидный формат номера

while True:
    number = input('Please enter the number :')
    if len(number)==10 and number.isdigit():
        print('The number {0} is valid'.format(number))
        break
    else:
        print('Input the correct number')
        continue

#Задача3
name='anton'
result=input('Please enter your name :')
if result.lower()==name:
    print('Yes its your name')
else:
    print('No its not')

