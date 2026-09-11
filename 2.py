"""
is_raining=True
if is_raining:
    print("Raining Outside")

else:
    print("Not Raining")



a = int(input("Enter your age : "))
if a>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")



a = int(input("Enter a number : "))
if a==1:
    print("Sunday")
elif a==2:
    print("Monday")
elif a==3:
    print("Tuesday")
elif a==4:
    print("Wednesday")
elif a==5:
    print("Thursday")
elif a==6:
    print("Friday")
elif a==7:
    print("Saturday")
else:
    print("Out of range number")



match a:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3: 
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Satuday")
    case _:
        print("Out of range number")



a = int(input("Enter your number : "))
if a%2==0:
    print("even")
else:
    print("odd")




a = int(input("Enter your age : "))

t=1010

if a>12:
    print("No discount, Payble amount is ",t)
else:
    print("10% Discount, Payble amount is ",t/100*90) # can be t-t//10




m = int(input("Enter your marks : "))
if m>=90 and m<=100:
    print("Grade : O")
elif m>=80 and m<=90:
    print("Grade : A")
elif m>=65 and m<=80:
    print("Grade : B")
elif m>=35 and m<=65:
    print("Grade : C")
elif m>100 or m<0:
    print("Invalid marks")
else:
    print("Grade : F")



a = int(input("Enter your number : "))
if a>0:
    print("Number is positive")
elif a==0:
    print("Number is 0")
else:
    print("Number is negative")

"""


a = int(input("Enter your number a : "))
b = int(input("Enter your number b : "))
c = int(input("Enter your number c : "))

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
elif c>a and c>b:
    print(c)
elif a==b==c:
    print("All are equal")
elif a==b and a>c:
    print("a and b are greatest : ",a)
elif c==b and c>a:
    print("c and b are greatest : ",c)
elif a==c and a>b:
    print("a and c are greatest : ",a)
