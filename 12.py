n = int(input("Enter a number : "))

x=0
for i in range(1,n+1):
    x+=i

print(x)




n = int(input("Enter a number : "))
# print(len(str(n)))

c=0
if n == 0:
    print(1)
else:
    while(n>0):
        c+=1
        n = n//10

    print(c)