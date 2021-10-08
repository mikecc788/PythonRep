class Cat(object):
    __cat_type = 'cat'
    def __init__(self,name):
        self.name = name

    def run(self):
        result = self.__run()
        print(result)

    def __run(self):
        return  f'小猫{self.name} happy run'

    def jump(self):
        result = self.__jump()
        print(result)

    def __jump(self):
        return  f'小猫{self.name} happy jump'

cat = Cat(name='cat')
cat.run()
cat.jump()
print(dir(cat))
print(cat._Cat__run()) #调用私有方法
class Test(object):
    pass

