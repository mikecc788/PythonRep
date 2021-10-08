class Person(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name} run')

    def jump(self):
        print(f'{self.name} jump')

xiaoming = Person(name='xiaoming',age=17)
xiaoming.jump()

li = Person(name='li',age=17)
li.top = 174
print(li.top)
