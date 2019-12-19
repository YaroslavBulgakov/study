import sys
import math
#sys.path.append(r'D:\Python_modules\my_module')
sys.path.append(r'D:\Python_modules')
DZ18_VAR1='Test1'
DZ18_VAR2='Test2'
print('------Content of match-----')
for attrib in dir(math):
    if not attrib.startswith('_'):
        print(attrib)
print('-----This module globals-----')
i=1
for i in globals().keys():
    print(i)
import my_module.my_funcs1 as funcs1
import my_module.my_classes1 as cls1
print('------my_funcs1 locals and globals------')
funcs1.some_func1()
t=cls1.TestClass(10,20)
print(t.add())

