def checkPerfectNumber(num: int) -> bool:
    a = 0
    for i in range(1,num):
        if num%i==0:
            a+=i

    if a == num:
        return True
    return False

print(checkPerfectNumber(60))