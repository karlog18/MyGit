import pandas as pd

x = [1.0, 1.6, 3.4, 4.0, 5.2]
y = [1.2, 2.0, 2.4, 3.5, 3.5]

def suma(a):
    sum = 0
    for i in range(len(a)):
        sum = a[i] + sum
    return sum

print(suma(x))
print(suma(y))

x1 = pd.array(x)
print(x1)

y1 = pd.array(y)
print(y1)

xy = x1 * y1
print(xy)

x2 = x1 * x1
print(x2)

n = len(x)
print(n)

def lin_reg(m, n):
    x = pd.array(m)
    y = pd.array(n)
    n = len(m)
    xy = x * y
    x2 = x * x

    a = (((n * suma(xy)) - (suma(x) * suma(y)))) / ((n * suma(x2)) - (n * (suma(x)* suma(x))))

    b = ((suma(y) * suma(x2)) - (suma(xy) * suma(x))) / ((n * suma(x2)) - (n * (suma(x)* suma(x))))
