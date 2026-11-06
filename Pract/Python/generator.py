def couunt_up_to(n):
    c = 1
    while c<=n:
        yield c
        c+=1
for i in couunt_up_to(5):
    print(i)


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a,b = b,(a+b)

a = fibonacci()
for _ in range(20):
    print(next(a))