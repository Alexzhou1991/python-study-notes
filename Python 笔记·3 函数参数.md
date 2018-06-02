
# 函数
    - 代码的一种组织形式
    - 一个函数一般完成一项特定的功能
    - 函数的使用
        ·函数需要先定义
        ·使用函数，俗称调用
        
    


```python
# 定义一个函数
# 只定义不执行
# 函数名自己定义。起名需要遵循命名规则
# 后面括号冒号不能少，括号内可以有参数
# 函数内所有代码缩进

def func():
    print('我是一个函数')
    print('我要完成一定功能')
    print('结束')
    
# 函数的调用
func()
```

    我是一个函数
    我要完成一定功能
    结束
    

## 函数的参数和返回值
    - 参数：负责给函数传递一些必要的数据或者信息
        ·形式参数(形参)：在函数定义的时候用到的参数没有具体的值。只是一个占位的符号
        ·实际参数(实参)：在调用的函数的时候输入的值
    - 返回值：函数的执行结果
        ·使用 return 关键字
        ·如果没有return ，默认返回一个None
        ·函数一旦执行到return 语句，则无条件返回，后面语句不再执行
        


```python
# 参数的定义和使用
# 参数person 只是一个符号，代表是调用的时候的某一个参数
# 调用的时候会用p的值代替函数中所有的person


def hello(person):
    print('{0},你咋回事'.format(person))
    print('I\'m good.')
p = input('请输入你的名字：')
hello(p)

```

    请输入你的名字：liu 
    liu ,你咋回事
    I'm good.
    


```python
# return 语句的基本使用
# 函数打完招呼后返回一句话

def hello(person):
    print('{0},你咋回事'.format(person))
    print('I\'m good.')
    
    return'{0}他很好，{1}没有问题'.format(person,person)
p = input('请输入你的名字：')
str = hello(p)
print(str)
```

    请输入你的名字：zhang
    zhang,你咋回事
    I'm good.
    zhang他很好，zhang没有问题
    


```python
# return 示例2

def hello(person):
    print('{0},你咋回事'.format(person))
    print('I\'m good.')
    return'{0}他很好，{1}没有问题'.format(person,person)
p = input('请输入你的名字：')
str = hello(p)
print(str)

```

    请输入你的名字：小张
    小张,你咋回事
    I'm good.
    小张他很好，小张没有问题
    


```python
# 九九乘法表 1.0

for row in range(1,10):  
    for col in range(1,row+1):
        print( row * col, end=' ')
    print('---')
```

    1 ---
    2 4 ---
    3 6 9 ---
    4 8 12 16 ---
    5 10 15 20 25 ---
    6 12 18 24 30 36 ---
    7 14 21 28 35 42 49 ---
    8 16 24 32 40 48 56 64 ---
    9 18 27 36 45 54 63 72 81 ---
    


```python
# 九九乘法表 2.0
# 定义一个函数，打印一行九九乘法表

def printline(row):
    for col in range(1,row+1):
        print( row * col, end=' ')
    print('-')
# 

for row in range(1,10):  
    printline(row)
```

    1 -
    2 4 -
    3 6 9 -
    4 8 12 16 -
    5 10 15 20 25 -
    6 12 18 24 30 36 -
    7 14 21 28 35 42 49 -
    8 16 24 32 40 48 56 64 -
    9 18 27 36 45 54 63 72 81 -
    

## 参数详解
    - 参数分类：
        ·普通参数
        ·默认参数
        ·关键字参数
        ·收集参数
        
    
### 普通参数
    - 定义的时候直接定义变量名
    - 调用的时候直接把变量或者值放入指定位置
    - 例
        def 函数名(参数1，参数2，....):
            函数体
        
        #调用
        函数名(value1,value2,....)   
        # 调用的时候按位置赋值 
        
### 默认参数
    - 形参带有默认值
    - 调用的时候，如果没有对相应形参赋值，则使用默认值
    - 例
        def func_name(p1=v1,p2=v2,....)
            func_block
        
        #调用1
        func_name()
        
        #调用2
        func_name(v1,v2,...)


```python
# 默认参数示例
# 包名函数，需要知道学生姓名，默认男生


def reg(name,age,gender='male'):
    if gender == 'male':
        print('{0}is {1}years old , he is good boy .'.format(name,age,gender))
    else:
        print('{0}is{1}years old , she , is good girl.'.format(name,age,gender))
        
# 调用
reg('小明',18)  # 默认参数可以不用填写
reg('小红',17,'female')   # 改动默认参数
```

    小明is 18years old , he is good boy .
    小红is17years old , she , is good girl.
    

### 关键字参数
    - 语法
        def func_name(p1=v1,p2=v2,...)
            func_body
            
        #调用函数
        func_name(p1=value1,p2=value2,....)
    - 好处：
        ·不容易混淆，
        ·是用关键字参数，可以不考虑参数位置
        




```python
# 普通参数示例

def stu(name,age,addr):    # 默认参数按照位置传递
    print('I am sutdent.')
    print('我叫{0},今年{1},住在{2}'.format(name,age,addr))

n = 'xiaoming'
a = 18
addr = 'beijing'
# 普通参数只按照位置传递，容易出错 
stu(n,a,addr)



# 关键字参数示例==============================================
def stu_key(name='no name',age=0,addr='no addr'):   #关键字参数在定义的时候赋值，执行默认
    print('I am sutdent.')
    print('我叫{0},今年{1}岁,住在{2}'.format(name,age,addr))

n = 'xiaoming'
a = 18
addr = 'beijing'
# 关键字参数可以打乱顺序，结果不变
stu_key(addr=addr,name=n,age=a)  #执行的时候重新赋值，可以不考虑顺序



```

    I am sutdent.
    我叫xiaoming,今年18,住在beijing
    I am sutdent.
    我叫xiaoming,今年18岁,住在beijing
    

###  收集参数
    - 把没有位置，不能和定义时的参数位置相对应的参数，放入一个特定的数据结构中
    - 语法
        def func_name(*args):
            func_body
            按照list使用方式访问args得到传入的参数
            
         #调用
         func_name(p1,p2,p3...)
        
    - args 可以自定义名称 ，但是必须要有星号，表示这是收集参数
    - 收集参数可以和其他参数共存
    - 收集参数可以不带任何实参调用，
    


```python
# 收集参数示例
# 函数模拟学生进行自我介绍，具体内容不清楚
# args 看做一个list

def stu(*args):
    print('Hello,下面是我的个人信息：')
    print(type(args)) # type 函数的作用是监测变量的类型
    for item in args:  # arges 变量放入 循环 中打印
        print(item)
stu('alex',18,'北京人','单身')   # 这个函数里参数较多
print('-' * 20) #分割线
stu('啥也不想说')  #  这个函数里就一个参数
print('-' * 20) #分割线
stu()  # 不带实参
```

    Hello,下面是我的个人信息：
    <class 'tuple'>
    alex
    18
    北京人
    单身
    --------------------
    Hello,下面是我的个人信息：
    <class 'tuple'>
    啥也不想说
    --------------------
    Hello,下面是我的个人信息：
    <class 'tuple'>
    


```python
# 关键字参数如果使用关键字参数格式调用，会出错
# 例
stu(name='liu')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-56-bd04e9a80411> in <module>()
          1 # 关键字参数如果使用关键字参数格式调用，会出错
          2 # 例
    ----> 3 stu(name='liu')
    

    TypeError: stu() got an unexpected keyword argument 'name'


### 收集参数之关键字收集参数
    - 把关键字参数按字典格式存入收集参数
    - 语法：
        def func_name(**kwargs):   # 收集参数一个* ， 关键字收集参数两个*
            func_body
            
        # 调用
        func_name(p1=v1,p2=v2,p3=v1,...)
            
    - kwargs 可自定义名称
    - 调用的时候，把多余的关键字参数放入kwargs 
    - 访问 kwaegs 需要按照字典格式访问  




```python
# 关键字收集参数示例
# 调用的时候要使用关键字参数

def stu( **kwargs):   # 收集参数一个* ， 关键字收集参数两个*
    print('Hello,一下是我的个人信息：')
    print(type(kwargs))
    for a,b in kwargs.items():   # a 是变量名称 b 是变量对应的值 kwargs 关键字参数后面要加.items()
        print(a,'===',b)
stu(name='alex',age=19,addr='beijing',brith="0920",tall=175)
print('-' * 20)
stu(name='Bob')
print('-' * 20)
stu()  # 收集参数可以为空

```

    Hello,一下是我的个人信息：
    <class 'dict'>
    name === alex
    age === 19
    addr === beijing
    brith === 0920
    tall === 175
    --------------------
    Hello,一下是我的个人信息：
    <class 'dict'>
    name === Bob
    --------------------
    Hello,一下是我的个人信息：
    <class 'dict'>
    

### 收集参数混合调用的顺序问题
    - 收集参数，关键字参数，普通参数可以混合使用
    - 使用规则就是，普通参数和关键字参数优先
    - 定义的时候一般找普通参数，关键字参数，收集参数tuple,收集参数dict
    


```python
# 收集参数混合调用示例
# 

def stu(name, age, *args, hobby='NO', **kwargs): # 普通参数，收集参数，关键字参数，关键字收集参数
    print('Hello ，以下是我的个人信息')
    print('我叫{0}，今年{1}岁了。'.format(name,age))
    if hobby == 'NO':
        print('我没啥爱好。')
    else:
        print('我的爱好是{0}'.format(hobby))
        
    print('.' * 10)
    
    for i in args:
        print(i)
        
    print('.' * 10)
    
    for k,v in kwargs.items():
        print(k,'---',v)
    
# 调用1
name = 'alex'
age = 19

stu(name,age)

print('-' * 20) #大分割线 -----------------

# 调用2

stu(name,age,hobby='旅游',)

print('-' * 20) #大分割线 -----------------

# 调用3

stu(name, age, 'kally', 'asina', hobby='旅游',hobby2='吃', hobby3='玩') # 普通参数值对应放入，其余的字符放入收集参数，=放入关键字收集参数


```

    Hello ，以下是我的个人信息
    我叫alex，今年19岁了。
    我没啥爱好。
    ..........
    ..........
    --------------------
    Hello ，以下是我的个人信息
    我叫alex，今年19岁了。
    我的爱好是旅游
    ..........
    ..........
    --------------------
    Hello ，以下是我的个人信息
    我叫alex，今年19岁了。
    我的爱好是旅游
    ..........
    kally
    asina
    ..........
    hobby2 --- 吃
    hobby3 --- 玩
    

###  函数文档
    - 函数文档的作用是对当前函数他供是用相关的参考信息
    - 文档的写法：在函数内部开始的第一行是用三引号进行定义
    - 函数文档的查看：
        · 使用help函数，例如： help(func_name)
        · 使用_doc_
     


```python
# 函数文档使用示例 

def stu(name, age, *args):
    '''
    这里是文档的注释内容
    :param name: 这里填写该函数参数1的描述
    :param age: 这里填写该函数参数2的描述
    :return: 这里填写返回值的描述
    '''
    print('*函数帮助文档示例*')
    
    
#查看函数帮助文档

help(stu)

print('-' * 20)

stu.__doc__
```

    Help on function stu in module __main__:
    
    stu(name, age, *args)
        这里是文档的注释内容
        :param name: 这里填写该函数参数1的描述
        :param age: 这里填写该函数参数2的描述
        :return: 这里填写返回值的描述
    
    --------------------
    




    '\n    这里是文档的注释内容\n    :param name: 这里填写该函数参数1的描述\n    :param age: 这里填写该函数参数2的描述\n    :return: 这里填写返回值的描述\n    '


