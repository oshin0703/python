#例外処理
def exception_test(value_1,value_2):
    print('====計算開始====')
    result = 0
    try:
        result = value_1 + value_2
    except:
        print('計算できませんでした!')
    finally:
        print('計算完了')

    return result

print(exception_test(100,200))
print(exception_test(100,'200'))

def exception_raise(value_1,value_2):
    print('====計算完了====')
    result = 0
    try:   
        result = value_1 + value_2
    except:
        print('計算できました!')
        raise
    finally:
        print('計算完了')
    return result

try:
    print(exception_raise(100,100))
    print(exception_raise(200,200))
    print(exception_raise(300,'300'))
except:
    print('エラーを受け取りました')

import os
import traceback

def exception_trace(value_1,value_2):
    print('====計算開始====')
    result = 0
    try:
        result = value_1 +value_2
    except:
        print('計算できませんでした!')
        raise
    finally:
        print('計算完了')
    return result

try:
    print(exception_trace(100,'200'))
except:
    print('----------------------')
    #print(traceback.format_exc(sys.exc_info()[2]))
    print('----------------------')