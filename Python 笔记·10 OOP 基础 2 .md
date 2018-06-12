
# 类和对象的成员分析

- 类存储成员是使用的 是与类关联的一个对象
- 独享存储成员是存储在当前对象中
- 对象访问一个成员是，如果对象中没有该成员，常识访问类中的同名成员，如果对象中有此成员一定使用对象中的成员
- 创建对象的时候，类中的成员不会放入对象当中，而是得到一个空对象，没有成员
- 通过对象对类中成员重新赋值或者通过对象添加成员时，对象成员会保存在对象中，而不会修改类成员


```python
# 类和对象实例 
# 此案例说明：类实例的属性和其对象的实例的属性在不对对象的实例属性赋值的前提下，指向同一个变量

class A():
    name = 'alex'
    age = 18
    
    def say(self):     # 参数有一个self
        self.name = 'aaaaaa'
        self.age = 200

# 此时，A成为类实例
print(A.name)
print(A.age)

print(id(A.name))
print(id(A.age))    

print('=' * 20)

a = A()

print(a.name)
print(a.age)

print(id(a.name))    # 这两个的ID 与A.name和A.age的ID一致，说明在不给实例赋值的情况下是同一个变量
print(id(a.age))  

a.name = 'Liu'
a.age = 200

print('=' * 20)

print(a.name)
print(a.age)

print(id(a.name))    # 给实例化的对象实例赋值之后，ID不一致，说明就不是用一个变量了
print(id(a.age))  
```

    alex
    18
    2767216109248
    1692823552
    ====================
    alex
    18
    2767216109248
    1692823552
    ====================
    Liu
    200
    2767216213888
    1692829376
    

# 关于self 

- self 在对象的方法中表示当前对象本身，如果通过对象调用一个方法，那么该对象会自动传入到当前方法的第一个参数中
- self 本身并不是关键字，只是一个用于接受对象的普通参数，理论上可以用任何一个普通变量名称代替
- 方法中有self 形参的方法称为非绑定类的方法，可以通过对象访问，没有self的是绑定类的方法，只能通过类访问
- 使用类访问绑定类的方法时，如果类方法中需要访问当前类的成员，可以通过__class__成员名来访问
- 


```python
# self 示例
class Student():
    name = 'alex'
    age = 18
    
    def say(self):    
        self.name = 'aaaaaa'
        self.age = 200
        print('my name is {0}'.format(self.name))
        print('my age is {0}'.format(self.age))
    
    def saysay(s):    
        print('my name is {0}'.format(s.name))   # 将self替换为s  ，此函数不变
        print('my age is {0}'.format(s.age))
stu = Student()
stu.say()

print('-' * 20)
stu.saysay()    # 将 s 替换为 self 后，此函数执行结果不变，说明self 可替代
        
```

    my name is aaaaaa
    my age is 200
    --------------------
    my name is aaaaaa
    my age is 200
    


```python
# 示例2 

class Teacher():
    name = 'Alex'
    age = 19
    
    def say(self):
        self.name = 'john'
        self.age = 17
        print('My name is {0}'.format(self.name))
        print('My age is {0}'.format(self.age))
    def saysay():
        print(__class__.name)     # 调用类的成员变量，要用__class__
        print(__class__.age)
        print('HHHHHHHHHHHHHHH')

t = Teacher()
t.say()
# 调用绑定类函数是用类名
Teacher.saysay()   # 直接使用 t.saysay() 则会报错


```

    My name is john
    My age is 17
    Alex
    19
    HHHHHHHHHHHHHHH
    


```python
# 关于self的案例

class A():
    name = 'alex'
    age = 19
    
    def __init__(self):
        self.name = 'john'
        self.age = 29
    def saysay(self):
        print(self.name)
        print(self.age)
        
class B():
    name = 'BBBBBBB'
    age = 99
        
a = A()
a.saysay()   # 此时系统会默认吧a作为第一个参数传入函数

A.saysay(a)  # 此时self 被 a 替换

A.saysay(B)  #此时传入的类示例B ，因为B有name 和age 属性，所以不会报错

# 以上代码，利用了鸭子模型 ： 不同的类，只要具有相同属性，就可以作为参数互传

```

    john
    29
    john
    29
    BBBBBBB
    99
    

## 面向对象的三大特性
- 封装
- 集成
- 多态

### 封装
- 封装就是对对象的成员进行访问限制
- 封装的三个级别
    - 公开，public
    - 受保护的，protected
    - 私有的，private
    - public , private , protected 不是关键字
    
- 判别对象的位置
    - 对象内部
    - 对象外部
    - 子类中
- 私有
    - 私有成员是最高级别的封装，只能在当前类或者对象中访问
    - 成员前面添加两个下划线即可
    - Python 的私有 不是真私有，是一种称为name mangling 的改名策略，可以使用对象._classname_attributename访问

- 受保护的封装
    - 受保护的封装是将对象成员进行一定级别的封装，然后在类中或者子类中都可以进行访问，但是在外部不可以
    - 封装方法：在成员名称前添加一个下划线即可

- 公开的，公共的 public 
    - 公共的封装实际对成员没有任何操作，任何地方都可以访问
    


```python
# 私有变量案例
class Person():
    name = 'alex'    # name 是公有的成员
    __age = 18      # __age 就是私有成员
    
p = Person()  
print(p.name)    # name 是公有成员，可以访问 
# print(p.__age)   __age 是私有成员，无法访问  此代码执行会报错

p._Person__age = 99       # 使用_classname_attributename  可以访问并传入变量
print(p._Person__age)
```

    alex
    99
    

###  继承
- 继承就是一个类可以获得另外一个类中的成员属性和成员方法
- 作用：减少代码，增加代码的复用功能，同时可以设置类与类直接的关系
- 继承与被继承的概念：
    - 被继承的类叫父类，也叫基类，也叫超类
    - 用于继承的类叫自类，也叫派生类
    - 继承与被继承一定存在一个is-a 关系
- 继承的特征
    - 所有的类都继承自object 类，即所有的类都是object的子类
    - 子类一旦继承父类，则可以试用父类中除私有成员外的所有内容。
    - 子类继承父类后并没有将父类成员完全赋值到子类中，而是通过引用关系访问调用
    - 子类中可以定义独有的成员属性和方法
    - 子类中定义的成员和父类成员如果相同，则优先使用子类成员
    - 子类如果想扩充父类的方法，可以在定义新方法的同时访问父类成员来进行代码重用，可以使用 [父类名.父类成员] 的格式来调用父类成员，也可以使用[super().父类成员]  的格式来调用

- 继承变量函数的查找顺序问题
    - 优先查找自己的变量
    - 没有则查找父类
    - 构造函数如果本类中没有定义，则自动查找调用父类构造函数
    - 如果本类有定义，则不再继续向上查找



```python
# 继承的语法
#在Python中，任何类都有一个共同的父类叫object
class Person():
    name = 'NoName'
    age = 0
    __score = 0  # 成绩是秘密只要自己知道，用两个下划线标注 
    _petname = 'secret'   # 小名，是保护的，子类可以用，但不能共用   用一个下划线
    def sleep(self):
        print('sleeping...')
    
class Teacher(Person):       # Teacher 就可以继承Person的子类     父类写在括号内   
    teacher_id = '9527'
    def make_test(self):    # 
        print('test.....')

t = Teacher()
print(t.name)            #    Teacher 里没有name ，但是继承了父类Person 里的
print(t._petname)       #   
# print(t.__score)     # 公开访问私有变量则会报错
t.sleep()             #  sleep 是父类方法，继承访问
print(t.teacher_id)  # teacher_id 是子类中独有的成员 
t.make_test()       # make_test()是子类类里独有的



```

    NoName
    secret
    sleeping...
    9527
    test.....
    


```python
# 子类父类相同成员的引用优先使用子类
class Teacher(Person):       # Teacher 就可以继承Person的子类     父类写在括号内   
    name = 'Alex'
    teacher_id = '9527'
    def make_test(self):    # 
        print('test.....')

t = Teacher()
print(t.name)     # 子类中定义的成员和父类成员如果相同，则优先使用子类成员
```

    Alex
    


```python
#  子类扩充父类功能的案例--------------------
class Person():
    name = 'NoName'
    age = 0
    def work(self):
        print('make money ...')
    
class Teacher(Person):     
    teacher_id = '9527'
    def make_test(self):   
        print('test.....')
    def work(self):         # 扩充父类的功能只需要调用父类相应的函数
        Person.work(self)  # 引用父类方法1
        super().work()    # 引用父类方法2
        self.make_test()

t = Teacher()
t.work()       # 引用了父类的方法，同时也有子类自己的方法 


```

    make money ...
    make money ...
    test.....
    

### 构造函数
- 是一类特殊的函数，在类进行实例化之前进行调用
- 如果定义了构造函数，则实例化时执行构造函数，不查找父类构造函数
- 如果没有定义，则自动查找父类构造函数
- 如果子类没有定义，负责的构造函数代参数，则构造对象时的参数应该按父类参数构造



```python
# 构造函数的概念 

class Dog():
    def __init__(self):     # __init__就是构造函数，每次实例化的时候第一个被调用,因为主要工作是进行初始化，所以得名
        print('I am init in dog')
        
kk = Dog()     #  实例化的时候就自动调用Dog的构造函数并执行

```

    I am init in dog
    


```python
# 继承中的构造函数

class Animal():
    def __init__(self):
        print('init in Animal')
class Pet():
    def __init__(self):
        print('I am init in Pet .')

class Dog(Pet):
    def __init__(self):
        print('I am init in Dog')
        
kk = Dog()  # 子类有构造函数，父类也有构造函数，首先调用自身的构造函数

class Cat(Pet):    #  字类中没有构造函数，父类是Pet
    pass 
        
mimi = Cat()   # 字类中没有构造函数，则调用父类的构造函数,在Pet中查找到构造函数，则停止向上查找

```

    I am init in Dog
    I am init in Pet .
    

### super  
- super 不是关键字，而是一个类
- super 的作用是获取MRO （）列表中的第一个类
- super 与父类没有直接任何实质性关系，但通过super可以调用到父类的成员
- super 使用的常用方法： 在构造函数中调用父类的构造函数

