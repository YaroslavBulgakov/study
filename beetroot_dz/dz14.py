def name_function(f):
    def wrapper(*args,**kwargs):
        print('The name of function is ',f.__name__)
    return wrapper
@name_function
def func1():
    print('Hello i am a func1')
@name_function
def func2():
    print('Hello i am a func2')

func1()
func2()