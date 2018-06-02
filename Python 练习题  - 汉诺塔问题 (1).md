

```python
# 汉诺塔代码

def hano(n,a,b,c):
    '''
    汉诺塔递归实现
    n：代表几个盘子
    a：代表第一个塔,
    b：代表第二个塔,
    c：代表第三个塔,
    '''
    if n == 1:
        print(a,'-->',c)
        return None
    if n == 2:
        print(a,'-->',b)
        print(a,'-->',c)
        print(b,'-->',c)
        return None
    
    hano(n-1,a,c,b)    # 把n-1 个盘子，从a借助于C塔，挪到B塔上去
    print(a,'-->',c)
    
    hano(n-1,b,a,c) # 把N-1个盘子，借助于A挪到C塔上

a = 'A'
b = 'B'
c = 'C'

n = int(input('输入盘子个数'))
hano(n,a,b,c)
```

    输入盘子个数6
    A --> B
    A --> C
    B --> C
    A --> B
    C --> A
    C --> B
    A --> B
    A --> C
    B --> C
    B --> A
    C --> A
    B --> C
    A --> B
    A --> C
    B --> C
    A --> B
    C --> A
    C --> B
    A --> B
    C --> A
    B --> C
    B --> A
    C --> A
    C --> B
    A --> B
    A --> C
    B --> C
    A --> B
    C --> A
    C --> B
    A --> B
    A --> C
    B --> C
    B --> A
    C --> A
    B --> C
    A --> B
    A --> C
    B --> C
    B --> A
    C --> A
    C --> B
    A --> B
    C --> A
    B --> C
    B --> A
    C --> A
    B --> C
    A --> B
    A --> C
    B --> C
    A --> B
    C --> A
    C --> B
    A --> B
    A --> C
    B --> C
    B --> A
    C --> A
    B --> C
    A --> B
    A --> C
    B --> C
    
