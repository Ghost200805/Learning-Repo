n = int(input("Enter a number : "))
list = []
if n<10:
    print(n)
else:
    while(n!=0):
        list += [n % 10]
        n//=10
a = "".join(map(str,list)) # Declare a as int to compare it or else fine....
print(*list,sep="") # or print(a)
