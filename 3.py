# a = True
# while a:
#     abc = input("Enter a string : ")
#     print(abc) 
#     a = False # Can use Break Also

# print("Congrats you are out of loop....")


# Counting no. of iterations...
a = int(input("Enter a number : "))
i = -10
b = 0
while i<=a:
    i+=1
    b+=1
    if i==a:
        print(b)


# Counting even and odd numbers....
b=1
e=0
o=0

while b<=a:
    if b%2==0:
        e+=1
    else:
        o+=1
    b+=1

print("Even : ",e,"Odd : ",o)


