#for文

for i in range(10):
    print(i)
for i in range(2,10):
    print(i)
for i in range(-2,10):
    print(i)


print('python', end=' ')
print('-', end=' ')
print('izm', end=' ')
print('com')

#テキストファイル作成
f_obj = open('test.txt','w')
print('python-izm.com',file=f_obj)

#フォーマット出力
print('Pythonの学習サイト : %s' % 'python-izm.com')
print('Pythonの学習サイト : %s-%s.%s' % ('python', 'izm', 'com'))

test_int = 100 + 100
test_str = 'python-izm.com'
print('サイト開設%d日目！%s'%(test_int,test_str))

print('Pythonの学習サイト　: {}'.format('python-izm.com'))
print('pythonの学習サイト　: {0}-{1}.{2}'.format('python','izm','com'))
test_int = 100 + 100
test_str = 'python-izm.com'
print('サイト開設{1}日目!{0}'.format(test_str,test_int))