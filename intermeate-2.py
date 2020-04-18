#

def test_1(*args):
    print(args)
test_1(1,2,3,4,5)

def test_2(code,name,*args):
    print(code,name)
    print(args)
test_2(100,'python-izm','JP','US')

def test_3(code,name,*countries):
    print(code,name)
    print(countries)
test_3(100,'python-izm','JP','US')

def test_4(**kwargs):
    print(kwargs)
test_4(code=100,name='python-izm')

def test_5(code,name,kana,*args,**kwargs):
    print(code,name,kana)
    print(args)
    print(kwargs)
test_5(100,'python-izm',u'パイソンイズム','JP','US',email = 'xxxx',city = 'Tokyo')