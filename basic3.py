#標準ライブラリ
import datetime

today = datetime.date.today()
todaydetail = datetime.datetime.today()

#今日の日付
print('今日の日付は'+str(today)+'です')
print(todaydetail)

print('-------------------')
print('今日は'+str(today.year)+'年'+str(today.month)+'月'+str(today.day)+'日です。')

# 日付のフォーマット
print('----------------------------------')
print(today.isoformat())
print(todaydetail.strftime("%Y/%m/%d %H:%M:%S"))
