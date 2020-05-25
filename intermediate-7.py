#新スタイルクラス
class NewStyleClassBase(object):
    def test_method(self,msg):
        print('NewStyleClassBase: {}'.format(msg))

#新スタイルクラスを継承
class NewStyleClass(NewStyleClassBase):
    def test_method(self,msg):
        print('NewStyleClass: {}'.format(msg))
        super(NewStyleClass,self).test_method(msg)

new = NewStyleClass()
new.test_method('method_call')