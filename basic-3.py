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
print('----------------------------------')

# 今日の日付
print('今日の日付')
print(today)
 
# 明日の日付
print('明日の日付')
print(today + datetime.timedelta(days=1))
 
newyear = datetime.datetime(2010, 1, 1)
 
# 2010年1月1日の一週間後
print('2010年1月1日の一週間後')
print(newyear + datetime.timedelta(days=7))
 
# 2010年1月1日から今日までの日数
print('2010年1月1日から今日までの日数')
#calc = today - newyear #ここでエラーが出る
 
# 計算結果の戻り値は「timedelta」
#print(calc.days)

import calendar

#うるう年かの判定
print(calendar.isleap(2015))
print(calendar.isleap(2016))
print(calendar.isleap(2017))

#指定期間内のうるう年の回数
print('指定期間内のうるう年の回数')
print(calendar.leapdays(2010,2020))