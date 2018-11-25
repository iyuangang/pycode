import random
 
class Fish:
    def __init__(self):
        self.x = random.randint(1,10)     #直接给出了实例变量的值，因此不需要参数了
        self.y = random.randint(1, 10)
    def move(self):
        self.x -= 1                       #重写self.x变量
        print("我的位置：",self.x,self.y)
 
class Goldfish(Fish):
    pass
 
class Shark(Fish):
    def __init__(self):
        Fish.__init__(self)                  #__init__后面跟的参数要与父类__init__后面的参数一致
        self.hungry = True
    def eat(self):
        if self.hungry == True:
            print("吃货的梦想就是天天吃")
            self.hungry = False
        else:
            print("吃不下了")
 
fish = Fish()
fish.move()                               #父类调用move()方法
 
goldfish = Goldfish()
goldfish.move()
goldfish.move()                           #self.x的值为上一次的-1
   
shark = Shark()
shark.eat()
shark.eat()
 
shark.move()
