

    
# 程序结构
    - 顺序
    - 分支
    - 循环
    
## 分支
    - 分支的基本语法
        if 条件表达式：
            语句1
            语句2
            语句3
            。。。。。
        条件表达式就是计算结果必须为布尔值的表达式
        表达式后面必须带冒号


```python
#if 语句 练习
#请输入年龄大小，大于18 ：你好，大孩子。小于18：小崽子
age = int(input('请输入年龄大小:'))
if age >=18:
    print('你好，大孩子')
else:
    print('小崽子')
```

    请输入年龄大小:17
    小崽子
    

### 双向分支
    - if...else...语句
    - 双向分支有两个分支，当程序执行到if...else...语句的时候，一定会执行if或者else中的一个，也只执行一个
    - input 返回的内容一定是字符串类型



```python
gender = input('请输入性别：')
print('您输入的性别是：{0}'.format(gender))

if gender == 'nan':
    print('你是个爷们')
else:
    print('你是个妹子')
print('开始上课')
```

    请输入性别：
    您输入的性别是：
    你是个妹子
    开始上课
    


```python
#成绩判断

score = int(input('请输入分数'))
if score >= 90:
    print('A')
if score <90 and score >=80:
    print('B')
if score <80 and score >=70:
    print('C')
if score <70:
    print('byebye!')
```

    请输入分数1000
    A
    

### 多路分支
    - 有很多分支情况，简称多路分支
    - elif 可以无限多
    - else 可以没有
    - 多路分支只执行一个。
    
    
## 循环语句
    -重复执行某些基本固定的事务
    -分类
        for 循环
        while 循环
        
### for 循环
    for 变量 in 序列：
        语句1
        语句2
        ...
    列表循环
    
    当for循环介乎的时候会执行else 语句（可选）
        


```python
#打印学生列表姓名
#如果是liuxiang ：世界冠军！  其他人BYEBYE !
#最后所有同学上课！
for name in ['xiaoli','xiaozhang','ergou','liuxiang',]:
    
    if name =='liuxiang':
        print('你好，偶像{0}'.format(name))
    else:
        print('{0}同学你好'.format(name))
else:
    print('所有同学开始上课！！！')
```

    xiaoli同学你好
    xiaozhang同学你好
    ergou同学你好
    你好，偶像liuxiang
    所有同学开始上课！！！
    

### 循环之 break ,contineu ,pass
    -break:无条件结束整个循环（循环猝死）
    -contineu : 无条件结束本次循环，从新进入下一轮循环
    -pass :略过 一般用于占位
    


```python
#break 语句示例
#寻找1到10 的数据，遇到 7 结束
for i in range(1,11):
    if i == 7:
        print('7找到了！')
        break
    else:
        print(i)
```

    1
    2
    3
    4
    5
    6
    7找到了！
    


```python
#break 语句示例
#打印1到10 中的 偶数

for i in range(1,11):
    if i % 2 == 1 :
        continue
    print('{0}是偶数！'.format(i))
```

    2是偶数！
    4是偶数！
    6是偶数！
    8是偶数！
    10是偶数！
    


```python
#pass 示例 

for i in range(1,11):
    pass
    print('略过')
```

    略过
    略过
    略过
    略过
    略过
    略过
    略过
    略过
    略过
    略过
    

### while 循环
    - 一个循环语句
    - 表示当某循环条件成立的时候进行循环
    - 不知道循环的次数，但能确定循环成立条件的时候使用while循环
    - while 循环语法：
    
        while 条件表达式:
            语句
            
            
        或者：
        
        while 条件表达式:
            语句1
        else:
            语句2
        
    


```python
# 假设年利率6.7% ， 本利是每年翻倍，则多少年后本钱会翻倍

benqian = 100000
year = 0
while benqian < 200000:
    benqian = benqian * (1+0.067)
    year += 1 # year = year + 1
    print('第{0}年拿了{1}块钱'.format(year,benqian))
else:
    print('本钱已经翻倍')
    
```

    第1年拿了106700.0块钱
    第2年拿了113848.9块钱
    第3年拿了121476.77629999998块钱
    第4年拿了129615.72031209998块钱
    第5年拿了138299.97357301068块钱
    第6年拿了147566.07180240238块钱
    第7年拿了157452.99861316333块钱
    第8年拿了168002.34952024528块钱
    第9年拿了179258.5069381017块钱
    第10年拿了191268.8269029545块钱
    第11年拿了204083.83830545243块钱
    本钱已经翻倍
    
