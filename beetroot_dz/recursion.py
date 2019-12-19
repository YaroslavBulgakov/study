def privet(n):
    #начнем сначала если х=0 то выйти
    if n==0:
        return
    else:
        print('Hello world')
        privet(n-1)
#Ну тут практически во всех обратный отсчет как мы видим
#Иначе мы фактиечски жестко зашьем условие в код если ну тут практически тоже но более логичей
privet(10)

def summa(x):
    #Очень важно всегда писать граничые значения
    if x==0:
        return 0
    if x==1:
        return 1
    else:
        #например закинули 4 вверху проверилось  потом она же в ретурне опять сама себя запускает вот че а не выходит стразу т.е в ретурн она будет крутиться
        #то есть потом поднимается по памяти и возвращается 2+1 потом 3+4 =
        return x+summa(x-1)

z=summa(4)
print(z)

def decimal_to_bin(n):
    result=str(n%2)
    if n<2:
        return result
    else:
        return decimal_to_bin(n//2)+result

print(decimal_to_bin(128))

#Это для любого преобразования
def decimal_to_any(n,my_base=2):
    result=n%my_base
    if result>9:
        #Это мы написали типа получить символ например если он 11
        #то А это у нас 10 отнимем 1 типа чтоб от 9-тиначать и прибавлем все что в результате больше 9
        result=chr(ord('A')-1+result-9)
    else:
        result=str(result)
    if n<my_base:
        return result
    else:
        return decimal_to_any(n//my_base,my_base)+result
#35 - это максимальное числокоторе у нас поддерживат int т.е 9 символов + 26
result=decimal_to_any(1280177132441,35)
print('Decimal to any ',result)
print(int('1280177132441',35))

def fib(i):
    a,b=0,1
    for c in range(i):
        a,b=b,a+b
        print(b,end='')


#Мой вариант с глобальной перменной меньше есть памяти