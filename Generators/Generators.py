def gen():
    for i in range(100000):
        yield i

x=gen()
for i in x:
    print(i)
