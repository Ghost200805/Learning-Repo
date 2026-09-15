a = int(input("Enter a number : "))

i=1
while i<=10:
    print(a,"x",i,"=",a*i)
    i+=1


start = int(input("Enter start: "))
end = int(input("Enter end: "))

n = start
while n <= end:
    i = 2
    count = 0
    while i < n:
        if n % i == 0:
            count += 1
        i += 1
    if n > 1 and count == 0:
        print(n)
    n += 1

