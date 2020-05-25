#クラス作成

class TestClass:
    def __init__(self,code,name):
        self.code = code
        self.name = name

classes = []
classes.append(TestClass(1,'test1'))
classes.append(TestClass(2,'test2'))

for test_cls in classes:
    print('===== Class =====')
    print('code -->'+str(test_cls.code))
    print('name -->'+test_cls.name)