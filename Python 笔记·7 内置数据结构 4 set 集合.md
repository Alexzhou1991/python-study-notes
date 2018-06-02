
# 集合- set 
    - 集合时候高中数学中的一个概念
    - 一堆确定的无需的唯一的数据，集合中每一个数据成为一个元素


```python
# 创建集合
s = {1,2,3,4,5,6}    # 大括号内要有值，如果大括号内没有值的话，创建出来的是dict 类型
s1 = {}
print(type(s))
print(type(s1))

s2 = set()      # 要创建空的集合，要用set赋值方式
print(type(s2))    

print(s)
```

    <class 'set'>
    <class 'dict'>
    <class 'set'>
    {1, 2, 3, 4, 5, 6}
    

## 集合的特征
    - 集合内数据无需，即无法索引和分片
    - 集合内数据元素具有唯一性，可以用来排除重复数据
    - 集合内的数据，str, int , float , tuple , 冻结集合等，及内部只能防止可哈希数据
    - 集合本身不可哈希

### 集合序列操作 
    - 成员检测：in , not in 
    - 集合遍历操作


```python
# 成员检测操作
s = {9,6,'john','kally','halo'}
print(s)           # 集合内的数据无序，打印出的结果与放入时的顺序不一致

if 'john' in s:    # set 成员检测与list 一致
    print('yes')
else:
    print('no')
```

    {'kally', 6, 9, 'john', 'halo'}
    yes
    


```python
# 集合遍历操作
s = {9,6,'john','kally','halo'}
for i in s:
    print(i,end=' ')
```

    kally 6 9 john halo 


```python
# 带有元祖的遍历
s = {(1,2,3),('one','two','three'),(7,8,9)}
for k,m,n in s:
    print(k,'---',m,'---',n)   # 多层遍历
for k in s:
    print(k)   # 单层遍历
```

    one --- two --- three
    7 --- 8 --- 9
    1 --- 2 --- 3
    ('one', 'two', 'three')
    (7, 8, 9)
    (1, 2, 3)
    

### 集合的内涵


```python
# 普通集合内涵
s = {12,23,34,45,1,2,2,1,1,2,2,}
print(s)   # 集合在初始化之后自动过滤掉重复值

ss = {i for i in s}     # 用集合创建集合
print(ss)

sss = {i for i in s if i % 2 == 0}   # 带条件的集合创建集合
print(sss)
```

    {1, 34, 2, 12, 45, 23}
    {1, 34, 2, 12, 45, 23}
    {34, 2, 12}
    


```python
# 多循环的集合内涵 
s1 = {1,2,3,4,5}
s2 = {'john','kally','tom','k','la'}
s = {m*n for m in s2 for n in s1}
print(s)

s = {m*n for m in s2 for n in s1 if n == 2}
print(s)
```

    {'tomtomtomtom', 'johnjohnjohn', 'lalalalala', 'john', 'kkk', 'tomtomtomtomtom', 'johnjohnjohnjohn', 'kally', 'tomtomtom', 'kkkk', 'johnjohnjohnjohnjohn', 'tomtom', 'kallykallykallykally', 'lalalala', 'kallykally', 'k', 'lalala', 'kallykallykally', 'kallykallykallykallykally', 'lala', 'la', 'kkkkk', 'tom', 'kk', 'johnjohn'}
    {'tomtom', 'lala', 'kk', 'johnjohn', 'kallykally'}
    

## 集合的函数/关于集合的函数
    - len,max,min  
    - 跟其他基本函数一致
    - add:向函数内添加元素
    - clear:清空 
    - copy 拷贝
    - remove 移除指定的值
    - discard 移除集合中指定的值
    - pop 随机移除一个元素


```python
# add示例
s = {1}
s.add(344)  # 向集合内添加一个元素
print(s)

s.clear()
print(s)   # 原地清空数据
```

    {344, 1}
    set()
    


```python
# remobe 和 discard 区别 
s = {1,2,3,4,5,6,7,8,9}
print(s)
s.discard(5)
print(s)

print('-'*20) #--------分割线--------

s.discard(999)  #  discard 一个不存在的值
print(s)

s.remove(888)   # remove一个不存在的值会报错
print(s)
```

    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 6, 7, 8, 9}
    --------------------
    {1, 2, 3, 4, 6, 7, 8, 9}
    


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-34-f63e8d9d5248> in <module>()
         10 print(s)
         11 
    ---> 12 s.remove(888)
         13 print(s)
    

    KeyError: 888



```python
#  pop 示例
s = {1,2,3,4,5,6,7,8}
d = s.pop()   # 移除一个元素，并赋值给d 
print(d)
print(s)
```

    1
    {2, 3, 4, 5, 6, 7, 8}
    

###  集合函数
    - intersection :交集
    - differrence ：差集
    - union ： 并集
    - issubset : 检查一个集合是否为另一个子集
    - isssuperset : 检查一个集合是否为另一个超集
    - 


```python
# intersection :交集  示例
s1 = {1,2,3,4,5,6,7}
s2 = {5,6,7,8,9,0}
i1 = s1.intersection(s2)    # 将s1 与 2s的交集赋值给s3 
print(i1)

i2 = s1.difference(s2)   # 将s1 与 s2 的差集赋值给s4 
print(i2)

i3 = s1.issubset(s2)   # 检查s1 是否为s2 的子集。结果为布尔值
print(i3)
```

    {5, 6, 7}
    {1, 2, 3, 4}
    False
    


```python
# 集合的数学操作
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}

s_1 = s1 - s2     # 集合之间可以减法操作 ，即 用S1里减去S1与S2的交集
print(s_1)

s_2 = s1 + s2   #  集合之间无法加法操作 
print(s_2)
```

    {1, 2, 3, 4}
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-42-52920de4e94f> in <module>()
          6 print(s_1)
          7 
    ----> 8 s_2 = s1 + s2
          9 print(s_2)
    

    TypeError: unsupported operand type(s) for +: 'set' and 'set'


###  frozen set : 冰冻集合
    - 冰冻集合就是不可以进行任何修改的集合
    - frozenset 是一种特殊集合


```python
# frozen 集合创建
s = frozenset()
print(type(s))
print(s)

```

    <class 'frozenset'>
    frozenset()
    
