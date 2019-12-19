def SquareGenerator(begin,end):

    if type(begin) is not int:
        print('Begin must be integer')
        return None
    if type(end) is not int:
        print('End number must be integer')
        return None
    if begin>end:
        print('Begin number must be greater than end')
        return None

    for num in range(begin,end+1):
        yield num**2

generator=SquareGenerator(1,12)
for i in generator:
    print(i)

print('----------------')
for i in generator:
    print(i)
