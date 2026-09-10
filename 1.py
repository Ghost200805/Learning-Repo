a = 10

print (11//5)

print(10/3)

#z = int(input("Enter your number : "))
#print("This is your number - ",z)

#print (a+z)

d= "Hello"
f = "World"
print(d+f)


# Program to convert minutes into hours

l = int(input("Enter Minutes : "))
print (l,"is",l//60,"hours",l%60,"minutes")

# Program to convert age in year to days

x = int(input("Enter Age : "))

j = x*365
"""for i in range (4,x,4):   # For Leap year
    j+=1
"""

print (f"{x}years = {j} days")

# Program to check if a number is odd or even without if else statements

m = int(input("Enter number : "))
zx = m%2
print ("Number is odd : ",bool(zx)) # if odd = true , if even = false



# Program to Extract last digit of a number

q = int (input("Enter number : "))
print(q,": last digit is",q%10)

# Program to swap 2 variable without a third variable using arithmatic operations

a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))

print ("Before swap : a=",a,",b=",b)

a += b
b = a - b
a -= b

print ("After swap : a=",a,",b=",b)


# Program to check if student is eligible to get the discount , catch is he must be student and must be less than age 21

a = str(input("Enter your role : "))
b = int(input("Enter your age : "))

print("Eligible :",a.lower()=="student" and b<21)