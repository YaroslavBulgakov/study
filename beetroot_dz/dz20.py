print(int('1101',2))

def recursive_string(s,index):
    try:
        print(s[index],end='')
    except IndexError:
        return
    recursive_string(s,index+1)


def backword_string(s,index):
    if index<0:
        return
    print(s[index], end='')
    backword_string(s,index-1)
recursive_string('Hello world',0)
print('\n')
backword_string('Hello world',len('Hello world')-1)

result_bin=[]


def decimal_to_binary(n):
    ostatok=n%2
    global result_bin
    result_bin.insert(0,ostatok)
    if n<2:
        return
    decimal_to_binary(n//2)

def decimal_to_binary2(n):
    if n<2:
        return
    ostatok = n % 2
    return [].append(decimal_to_binary(n//2))

print('asas',decimal_to_binary2(13))
decimal_to_binary(13)
#print(result_bin)
print('\n------------')
result=''.join([str(x) for x in result_bin])
print(result)
print('Result is ',int(result,2))

#1,1,2,3,5,8,13,21,34

def fibonacci(n):

    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def feb2(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
        print(a)
    return a

feb2(8)
print('--------------')
i=0
def fib_recurse(n,a=1,b=1):
    global i
    if i==n:
        return a
    print(a)
    a, b = b, a + b
    i+=1
    fib_recurse(n,a,b)
fib_recurse(8)
#print(fibonacci(8))
