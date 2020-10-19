import timeit
import time


def func1(n):
    return [str(num) for num in range(n)]


def func2(n):
    return list(map(str,range(n)))


start_time = time.time()
func1(100000)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)
start_time = time.time()
func2(100000)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)
print(func2(10))
print(map(str,range(10)))

stmt = '''
func1(100)
'''

setup = '''
def func1(n):
    return [str(num) for num in range(n)]
'''
print(timeit.timeit(stmt, setup, number=100000))


stmt = '''
func2(100)
'''

setup = '''
def func2(n):
    return list(map(str,range(n)))
'''
print(timeit.timeit(stmt, setup, number=100000))
