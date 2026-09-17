# def recursion(n):
#     print(n)
#     if n<=0:
#         return
#     recursion(n-1)
        
# recursion(10)





# def factorial(n):
#     if n ==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))






s = lambda n: n*n

print(s(5))


a = lambda n,m : n+m

print(a(5,10))

sub = lambda n,m: n-m

print(sub(20,10))



# Crazy logic -


def fun(n):
    if n == 0:
        return

    fun(n-1)
    print(n)

fun(5)