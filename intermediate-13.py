#ファイルの読み書き
fr = open('read.txt','r',encoding="utf-8")

for row in fr:
    print(row)
fr.close()

fw = open('write.txt','w')
fw.write('Pythonでファイルに書き込みました！')
fw.close()

#文字コード変更
fin_utf = open('read.txt','r',encoding='utf-8')
fout_euc = open('euc-jp.txt','w',encoding='euc_jp')
fout_sjis = open('sjis.txt','w',encoding='shift-jis')
for row in fin_utf:
    fout_euc.write(row)
    fout_sjis.write(row)
fin_utf.close()
fout_euc.close()
fout_sjis.close()