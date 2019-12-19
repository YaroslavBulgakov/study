
#Задача1
ls=[x**2 for x in range(1,101) ]
print(ls)
#Задача2
cars=list()
while True:
    answer=input('Please input the car name :')
    if answer=='q':
        break
    cars.append(answer)
print(cars)

#Задача 3
#первый вариант
ls=[x for x in range(1,11)]
print(ls,len(ls))
i=len(ls)-1

while i!=-1:
    print(ls[i],end=' ')
    i-=1

#второй вариант
print('\n')
for i in range(len(ls)-1,-1,-1):
    print(ls[i],end=' ')



