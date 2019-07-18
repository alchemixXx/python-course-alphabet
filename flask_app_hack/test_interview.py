def a():
    print('test')
    for i in range(10):
        yield i


for i in a():
    print(i)
