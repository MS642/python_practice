import random


def gen_fibo(n):
    a = 1
    b = 1
    for x in range(n):
        yield a
        a, b = b, a+b


for x in gen_fibo(10):
    print(x)

s = 'hello'
for c in s:
    print(c)

it = iter(s)

print(next(it))
print(next(it))

for c in s:
    print(c)

print(next(it))


def gensquares(N):
    for x in range(N):
        yield x**2


for x in gensquares(10):
    print(x)

random.randint(1,10)


def rand_num(low,high,n):

    for i in range(n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)


# Generator Comprehension
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
