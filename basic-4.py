#配列・連想配列

#<タプル>要素数が決まっていて、追加削除できない
import datetime

def get_today():
    today =  datetime.datetime.today()
    value = (today.year,today.month,today.day)

    return value
test_tuple = get_today()
print(test_tuple)
print(test_tuple[0])
print(test_tuple[1])
print(test_tuple[2])





#<リスト>要素数が決まっていて、追加削除できる
test_list_1 = ['python','-','izm','.','com']
print(test_list_1)
print('-----------------------')
for i in test_list_1:
    print(i)
#要素の追加
#append
test_list_1 = []
print(test_list_1)
print('----------------------')
test_list_1.append('python')
test_list_1.append('-')
test_list_1.append('izm')
test_list_1.append('.')
test_list_1.append('com')
print(test_list_1)
#insert
test_list_1 = ['python', 'izm', 'com']
print(test_list_1)
print('--------------------------------')
test_list_1.insert(1,'-')
test_list_1.insert(3,'.')
print(test_list_1)
test_list_1.insert(0,'http://www.')
print(test_list_1)
#要素の削除
#remove
test_list_1 = ['1','2','3','2','1']
print(test_list_1)
print('------------------')
test_list_1.remove('2')
print(test_list_1)
#pop
test_list_1 = ['1','2','3','2','1']
print(test_list_1)
print('------------------')
print(test_list_1.pop(1))
print(test_list_1)
print(test_list_1.pop())
print(test_list_1)
#要素のインデックス取得
test_list_1 = ['100', '200', '300', '200', '100']
print(test_list_1.index('200'))
#要素数取得
test_list_1 = ['100', '200', '300', '200', '100']
print(test_list_1.count('200'))






#<ディクショナリ>keyとvalueがセットで一つの要素
test_dict_1 = {'YEAR':'2010', 'MONTH':'1', 'DAY':'20'}
print(test_dict_1)
print('=================================')
for i in test_dict_1:
    print(i)
    print(test_dict_1[i])
    print('------------------------------')

test_dict_1 = {'YEAR':'2010', 'MONTH':'1', 'DAY':'20'}
print(test_dict_1)
print('=================================')
print(test_dict_1['YEAR'])
#print(test_dict_1['YEARS'])
print('---------------------------------')
print(test_dict_1.get('YEAR'))
print(test_dict_1.get('YEARS'))
print('---------------------------------')
print(test_dict_1.get('YEAR','NOT FOUND'))
print(test_dict_1.get('YEARS','NOT FOUND'))
#要素の追加
test_dict_1 = {}
print(test_dict_1)
print('=================================')
test_dict_1['YEAR']  = '2010'
test_dict_1['MONTH'] = '1'
test_dict_1['DAY']   = '20'
print(test_dict_1)
#要素の削除
test_dict_1 = {'YEAR':'2010', 'MONTH':'1', 'DAY':'20'}
print(test_dict_1)
print('=================================')
del test_dict_1['DAY']
print(test_dict_1)
print('=================================')
#key、valueだけを取得
test_dict_1 = {'YEAR':'2010', 'MONTH':'1', 'DAY':'20'}
print(test_dict_1)
print('=================================')
print(test_dict_1.keys())
print(test_dict_1.values())
print('=================================')
#key,value同時に取得
test_dict_1 = {'YEAR':'2010', 'MONTH':'1', 'DAY':'20'}
print(test_dict_1)
print('=================================')
for key,value in test_dict_1.items():
    print(key,value)
print('=================================')
#keyの保持を確認
test_dict_1 = {'YEAR':'2010', 'MONTH':'1', 'DAY':'20'}
print(test_dict_1)
print('=================================')
print('YEAR' in test_dict_1)
print('YEARS' in test_dict_1)




#<セット>要素の追加削除は可能だが重複は禁止
test_set_1 = {'python', '-', 'izm', '.', 'com'}
print(test_set_1)
print('--------------------------------')
for i in test_set_1:
    print(i)
test_dict={}    #これはディクショナリ
test_set = {'python'}   #これはセット
empty_set = set()   #空のセットの作り方
test_set_1 = {'python', '-', 'izm', '.', 'com', 'python', 'izm'}
print(test_set_1)
print('--------------------------------')
for i in test_set_1:
    print(i)
#要素の追加
test_set_1 = set()
test_set_1.add('python')#単一要素の追加はadd
test_set_1.update({'-','izm','.','com'})#タプル、リスト等からの追加はupdate
print(test_set_1)
#要素の削除
test_set_1 = {'python', '-', 'izm', '.', 'com'}
test_set_1.remove('-')  #もともと指定した要素がない場合エラーがでる
test_set_1.discard('.') #もともと指定した要素がない場合エラーがでない
#frozenset・・・要素の削除や追加ができないセット
test_set_1 = frozenset({'python', '-', 'izm', '.', 'com'})
# test_set_1.remove('-')    #AttributeError
# test_set_1.discard('.')   #AttributeError
print(test_set_1)



#スライス   シーケンスから範囲を指定して要素を取得できる
# #sequence[<開始位置>:<終了位置>:<ステップ幅>]
test_list = ['https', 'www', 'python', 'izm', 'com']
print(test_list[:])
print(test_list[::])
print(test_list[:4])    #初めから4まで
print(test_list[2:])    #2から最後まで
print(test_list[::2])   #ステップ幅2
print(test_list[3:5])   #3から5
print(test_list[-1:])   # 末尾から１つ
print(test_list[:-1])   # 末尾から1つまで
print(test_list[::-1])  # 末尾から全ての逆順要素
print(test_list[:999])
#要素を代入
test_list[1:3] = ('WWW', 'PYTHON')
print(test_list)