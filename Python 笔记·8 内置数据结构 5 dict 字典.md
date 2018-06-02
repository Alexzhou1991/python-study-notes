
# dict  字典
    - 字典是一种组合数据，没有顺序的组合数据，数据以键值对形式出现


```python
# 创建空字典

d = {}
print(d)

d = dict()
print(d)


# 创建带值的字典
d = {'one':1,'two':2,'three':3}      # 键和值用冒号隔开
print(d)

d = dict(one=1,two=2,three=3)  # 利用关键字参数
print(d)

d = dict([('one',1),('two',2),('three',3)])  # 列表内嵌套元祖
print(d)
```

    {}
    {}
    {'one': 1, 'two': 2, 'three': 3}
    {'one': 1, 'two': 2, 'three': 3}
    {'one': 1, 'two': 2, 'three': 3}
    

## 字典的特征
    - 字典是序列类型，但是是无序序列，所以没有分片和索引
    - 字典中的数据每个都有键值对组成，即kv对
        - key:必须是可哈希的值，比如int,string,float,tuple,但是list,set,dict 不行
        - value：任何值 
        
        

## 字典常见操作






```python
# 访问数据
d = {'one':11111,'two':22222,'three':33333}  
print(d['one'])    #  访问格式：中括号内对应的键值，只打印对应键的值 
```

    11111
    


```python
# 重新赋值
d['three']='thrid' 
print(d)
```

    {'one': 11111, 'two': 22222, 'three': 'thrid'}
    


```python
# 删除某个操作
del d['two']
print(d)
```

    {'one': 11111, 'three': 'thrid'}
    


```python
# 成员检测 ： in , not in 
d = {'one':11111,'two':22222,'three':33333}  
if 2 in d:
    print('值')
if 'two' in d:
    print('键')        # 字典的成员检测只检测键  key   
if ('three',33333) in d:
    print('键值对')
```

    键
    


```python
# 字典的遍历
d = {'one':1,'two':2,'three':3}  
for k in d:
    print(k)  # 是用for 循环，直接按KEY值访问

print('-'*20)  # ----------分割线--------

for k in d.keys():
    print(k,d[k])   
    
print('-'*20)  # ----------分割线--------

for v in d.values():
    print(v)      #  只访问字典的值

print('-'*20)  # ----------分割线--------

for k,v in d.items():
    print(k,'---',v)  # 使用items  访问字典的键和值
```

    one
    two
    three
    --------------------
    one 1
    two 2
    three 3
    --------------------
    1
    2
    3
    --------------------
    one --- 1
    two --- 2
    three --- 3
    

### 字典生成式



```python
# 常规字典生成式
d = {'one':1,'two':2,'three':3}  
dd = {k:v for k,v in d.items()}
print(dd)
```

    {'one': 1, 'two': 2, 'three': 3}
    


```python
# 加限制条件字典生成式
ddd = {k:v for k,v in d.items() if v % 2 == 1}   # 加限制条件，仅限值是奇数的字典赋值给ddd 
print(ddd)
```

    {'one': 1, 'three': 3}
    

## 字典的相关函数
    - 通用函数： len,max,min,dict
    - clear 清空字典
    - items 返回字典的键值对 组成的元祖格式
    - keys 返回字典的键组成的一个结构
    - values 返回字典值组成的一个结构
    - get 根据指定建返回相应的值
        - get 好处是可以设置默认值
    - fromkeys 使用指定的序列作为键，使用一个值作为字典的所有键的值
    


```python
 # items 示例 
d = {'one':1,'two':2,'three':3}  
i = d.items()
print(type(i))
print(i)
```

    <class 'dict_items'>
    dict_items([('one', 1), ('two', 2), ('three', 3)])
    


```python
# keys 示例
k = d.keys()    # 将d 里的关键字 返回给K 
print(type(k))
print(k)
```

    <class 'dict_keys'>
    dict_keys(['one', 'two', 'three'])
    


```python
# values 示例
v = d.values()   # 只返回字典内的值
print(type(v))
print(v)
```

    <class 'dict_values'>
    dict_values([1, 2, 3])
    


```python
# get 示例 
d = {'one':1,'two':2,'three':3} 
print(d.get('nothere'))   # 返回字典内指定关键字对应的值，没有的话返回一个none 
print(d.get('three'))
print(d.get('nothere',99999))   #  带默认值，如果查找不到对应的键，则返回里面设置的值
print(d['nothere']) # 若直接访问一个不存在的键，则会报错
```

    None
    3
    99999
    


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-50-4149a27972f4> in <module>()
          4 print(d.get('three'))
          5 print(d.get('nothere',99999))
    ----> 6 print(d['nothere']) # 若直接访问一个不存在的键，则会报错
    

    KeyError: 'nothere'



```python
# fromkeys 示例
l = ['AAA','BBB','CCC']           # 生成一个列表
d = dict.fromkeys(l,'999')  #  将列表内的值都作为键，所有键对应的值都是‘999’
print(d)



```

    {'AAA': '999', 'BBB': '999', 'CCC': '999'}
    




--------------------