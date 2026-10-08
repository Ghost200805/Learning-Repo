def calculateElectricityBill(units: int) -> float:
    a = 0;
    if units < 0 :
        return -1.0
    elif units>=0:
        for i in range(units+1):
            if i <= 100 and i >= 1:
                a +=1.5
            elif i<=200 and i>=101:
                a+=2.5
            elif i<=300 and i>= 201:
                a+=4
            elif i>300:
                a+=5
        return round(a+50.0,2)

print(calculateElectricityBill(650))