
# 元组-tuple
    - 元祖可以看成是一个不可能改的list 
    - 元祖是小括号()
    
## 元组创建


```python
# 创建元组
t = ()     #  创建空的元组
print(type(t))

print('-' * 20)      # ---------分割线-----------

t = (9)    # 元组里只有一个值
print(type(t))   # 元元组内只有一个数值，打印出来的类型是int 

print('-' * 20)      # ---------分割线-----------

t = (9 ,)     # 元组内有多个值，或者加逗号，类型就是tuple
print(type(t))
print(t)
```

    <class 'tuple'>
    --------------------
    <class 'int'>
    --------------------
    <class 'tuple'>
    (9,)
    


```python
# 是用其他结构创建元组
l = [1,2,3,4,5,6]   # 创建一个表
t = tuple(l)       # 把表当成元组赋值给t 
print(type(t))    # t 的类型就是元组
print(t)         # t 的内容就是l的内容
```

    <class 'tuple'>
    (1, 2, 3, 4, 5, 6)
    

## 元组的特性
    - 是序列表， 有序
    - 元组数据值可以访问，不能修改
    - list 所有特性，除了可以修改外，元组都具有
    - list 的所有，分片，序列相加，相乘，成员资格操作等一样。
    


```python
# tuple 索引操作
t = (1,2,3,4,5)    #生成元组
print(t)
print(t[4])       # 索引第五个值

```

    5
    (1, 2, 3, 4, 5)
    


```python
# 超标错误
print(t[12])   # 索引超出元组内位置值会报错
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-14-776a01186cf7> in <module>()
          1 # 超标错误
    ----> 2 print(t[12])   # 索引超出元祖内位置值会报错
    

    IndexError: tuple index out of range



```python
# 切片操作
t = [1,2,3,4,5,6,7]
t1 = t[1:12]     #  对元组的切片操作可以超标
print(t1)
```

    [2, 3, 4, 5, 6, 7]
    


```python
# 序列相加
t1 = (1,2,3)
t2 = (4,5,6,)
t1 = t1 + t2   # 传址操作，将t2的内容扩展到t1 里 
print(t1)
```

    (1, 2, 3, 4, 5, 6)
    


```python
t1[1] = 9  #将t1 内的第二个数值修改为9，报错，因为tuple 不可修改
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-22-760b65281cc4> in <module>()
    ----> 1 t1[1] = 9  #将t1 内的第二个数值修改为9，报错，因为tuple 不可修改
    

    TypeError: 'tuple' object does not support item assignment



```python
# 元组相乘
t = (1,2,3)
t = t * 3
print(t)
```

    (1, 2, 3, 1, 2, 3, 1, 2, 3)
    


```python
# 成员检测 
t = (1,2,3,4,5,6)
k = int(input('输入要查找的数值：'))
if k in t:
    print('yes')
else:
    print('No')
```

    输入要查找的数值：9
    No
    


```python
# 元组遍历 ，一遍采用for 
# 1.单层元组遍历
t = (1,2,3,'john','kally','jack')
for i in t:
    print(i)
```

    1
    2
    3
    john
    kally
    jack
    


```python
# 2. 双层元组的遍历
t = ((1,2,3),('alex','john',999),(9,8,'kally'))
for i in t:
    print(i)   # 与单层元组遍历方法一样，但是结果为多层元组
    
print('-' * 20)      # ---------分割线-----------
    
for k,v,m in t:
    print(k,'===',v,'===',m)   # 多层元组遍历
```

    (1, 2, 3)
    ('alex', 'john', 999)
    (9, 8, 'kally')
    --------------------
    1 === 2 === 3
    alex === john === 999
    9 === 8 === kally
    

## 关于元组的函数
    - len:获取长度
    - 


```python
# len 获取元祖的长度 
t = (1,2,3,4,5)
len(t)
```




    5




```python
# max,min 最大值最小值
print(max(t))
print(min(t))
```

    5
    1
    


```python
# tuple 转化或创建元组
l = [1,2,3,4,5,6]
t = tuple(l)
print(t)
```

    (1, 2, 3, 4, 5, 6)
    

## 元组的函数
    - 基本跟list 通用



```python
# count 计算特定数据出现的次数
t = (1,2,3,1,5,4,5,4,1,5,2)
print(t.count(1))

# index,求特定元素在元祖中的索引位置
print(t.index(5))
```

    3
    4
    


```python
# 元祖变量交换  两个变量交换值
a = 1 
b = 3
print(a,'a')
print(b,'b')
a,b = b,a     # a的值和b的值进行交换
print(a,'a')
print(b,'b')
```

    1 a
    3 b
    3 a
    1 b
    
