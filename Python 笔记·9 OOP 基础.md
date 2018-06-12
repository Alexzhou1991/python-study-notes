
#  OOP- python面向对象
- python的面向对象
- 面向对象编程:
    - 基础
    - 公有私有
    - 继承
    - 组合 Mixin
 - 魔法函数
    - 魔法函数概述
    - 构造类魔法函数
    - 运算类魔法函数


# 面向对象概述(OpjectOriented,OO)
- OOP 思想：

    - 接触到任意一个任务，首先想到的是这个任务的构成，是由模型构成的
        
- 名词
    - OO：面向对象
    - OOA: 面向对象的分析
    - OOD：面向对象的设计
    - OOI：XXX的实现
    - OOP：XXX的编程
    - OOA->OOD->OOI :面向对象的实现过程
    
    
##  类和对象的概念
- 类：抽象名词，代表一个集合，共性的事物
- 对象：具象的事物，单个个体
- 类跟对象的关系：
    - 一个具象，代表一类事物的某一个个体
    - 一个是抽象，代表的是一大类事物
- 类中的内容，应该具有两个内容
    - 表明事物的特征，叫做属性（变量）
    - 表明事物功能或动作，称为成员方法（函数）
    
    
## 类的基本实现
### 类的命名
    - 遵守变量命名的规范
    - 大驼峰（首字母大写，单词直接相连）
    - 尽量避开跟系统命名相似的命名
### 如何声明一个类
    - 必须用class 关键字
    - 类由属性和方法构成，其他不允许出现
    - 成员属性定义可以直接使用变量赋值，如果没有值，使用None
    - 案例


```python
# 定义一个空的类
class Student():
    #一个空类，pass 代表直接跳过（必须pass）
    pass
    
# 定义一个对象
alex = Student()

# 再定义一个类，用来描述听Python的学生：
class PythonStudent():
    name = None     # 用None给不确定的值赋值
    age = 18       # 成员属性
    course = 'Python'
    
    # 注意缩进层级
    def DoHomeWork(self):       # 类里放函数（成员方法）
        print('I do Homework')

        return None 

# 实例化ALEX学生，是一个具体的人
alex = PythonStudent()     # 实例化一个对象 

print(alex.name)
print(alex.age)
alex.DoHomeWork()
```

    None
    18
    I do Homework
    

### 实例化类
    - 变量 = 类名()       #实例化了一个对象
### 访问对象成员
    - 使用点操作符
        - obj.成员属性名称
        - obj.成员方法
    - 可以通过默认内置变量检查类和对象的所有成员
        - 对象所有成员检查
            - #dict 前后各有两个下划线
            - obj.__dict__
        - 类所有的成员
            - # dict 前后各有两个下划线
            - class_name.__dict__


```python
#  实例
class Student():
    name = 'alex'
    age = 21
    
Student.__dict__   #  用__dict__ 查看类示例的内容

john = Student()    # 实例化

```




    mappingproxy({'__dict__': <attribute '__dict__' of 'Student' objects>,
                  '__doc__': None,
                  '__module__': '__main__',
                  '__weakref__': <attribute '__weakref__' of 'Student' objects>,
                  'age': 21,
                  'name': 'alex'})


