def my_favourite(movie_name):
    print('My favourite movie is',movie_name)
my_favourite('Assa')

def make_country(country,capital):
    dc={country:capital}
    print(dc)
make_country('France','Paris')

def calc(*args):
    operators=['+','-','*','/']
    operator=args[0]
    digits=args[1:]

    if args[0] not in operators:
        print('First argument must be operator one of {0}'.format(operators))
        return
    i=1
    while i<len(args):
        if type(args[i]) is not int:
            print('Argumnet in position {0} must be integer'.format(i+1))
            return
        i+=1
    if operator=='+':
        result = digits[0]
        for x in digits[1:]:
            result += x
        return result
    if operator=='-':
        result=digits[0]
        for x in digits[1:]:
            result-=x
        return result
    if operator=='*':
        result=digits[0]
        for x in digits[1:]:
            result*=x
        return result
    if operator=='/':
        result=digits[0]
        for x in digits[1:]:
            result/=x
        return result

print(calc('+',1,2,3,4,6))
print(calc('-',1,2,3,4,6))
print(calc('*',1,2,3,4,6))
print(calc('/',1,2,3,4,6))