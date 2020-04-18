#関数・メソッド

def test_func():
    print('call test_func')
test_func()

def cal(num_1,num_2,oprn):
    if oprn == 1:
        print('足し算開始')
        print(num_1 + num_2)
    elif oprn == 2:
        print('引き算開始')
        print(num_1 - num_2)
    elif oprn == 3:
        print('掛け算開始')
        print(num_1 * num_2)
    elif oprn == 4:
        print('割り算開始')
        print(num_1/num_2)
    else:
        print('不明なオプション指定です')
    
cal(100,10,3)

def cal2(num_1,num_2,oprn = 1):
    if oprn == 1:
        print('足し算開始')
        print(num_1 + num_2)
    elif oprn == 2:
        print('引き算開始')
        print(num_1 - num_2)
    elif oprn == 3:
        print('掛け算開始')
        print(num_1 * num_2)
    elif oprn == 4:
        print('割り算開始')
        print(num_1/num_2)
    else:
        print('不明なオプション指定です')
    
cal2(100,10)
cal2(100,10,4)

class TestClass:
    def test_method():
        print('call test_method')

print('--------------------')
print(test_func)
print(TestClass.test_method)

print('--------------------')
print(type(test_func))
print(type(TestClass.test_method))

print('------------------')
t = TestClass()
print(test_func)
print(t.test_method)