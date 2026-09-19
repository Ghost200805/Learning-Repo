for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()



print("\n")


for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()


print("\n")

for i in range(5):
    for j in range(i+1):
        print(j+1, end=" ")
    print()


print("\n")

for i in range(5,0,-1):
    for j in range(i):
        print(j+1, end=" ")
    print()


print("\n")



x = 1
for i in range(5):
    for j in range(i+1):
        print(x, end=" ")
        x=x+1
    print()


print("\n")


x = 21
for i in range(6,0,-1):
    for j in range(i):
        print(x, end=" ")
        x=x-1
    print()