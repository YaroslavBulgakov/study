#Задача1
import random
ls1=[]
ls2=[]
for i in range(0,10):
    ls1.append(random.randint(1,10))
    ls2.append(random.randint(1,10))
print('----------------Initial lists------------------')
print(ls1)
print(ls2)
print('------------------------------------------------')
s1=set(ls1)
s2=set(ls2)
print('In ls1 and ls2 elements :',s1.intersection(s2))

print('Остаток от деления ',35%8)

#Задача2
ls1=[x for x in range(0,100)]
ls2=[]
for x in ls1:
    if x%7==0:
        if x%5!=0:
            ls2.append(x)
print('Result list is',ls2)
