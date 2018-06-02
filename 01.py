'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
    #一个空类，pass 代表直接跳过（必须pass）
    pass
    
# 定义一个对象
alex = Student()

# 再定义一个类，用来描述听Python的学生：
class PythonStudent():
    name = None     # 用None给不确定的值赋值
    age = 18
    course = 'Python'
    
    # 注意缩进层级
    def DoHomeWork():
        print('I do Homework')

        return None 

# 实例化ALEX学生，是一个具体的人
alex = PythonStudent()

print(alex.name)
print(alex.age)
alex.DoHomeWork