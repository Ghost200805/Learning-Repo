def countFreq(n: int) -> list[int]:
    a = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    while n>0:
        a[n%10]+=1
        n//=10
    return list(a.values())
print(countFreq(76543))