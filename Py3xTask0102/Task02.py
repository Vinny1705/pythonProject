# Program to find leap year

year = 2005
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(year, " is a Leap year")
else:
    print(year, "is not a leap year")

# Program to find triangle classifier: isosceles, scalene or equilateral
a = 30
b = 70
c = 30
if ((a == b) and (b != c)) or ((b == c) and (c != a)) or ((c == a) and (c != b)):
    print("Isosceles triangle with sides", a, b, c)
elif (a == b) and (b == c) and (c == a):
    print("Equilateral triangle with sides", a, b, c)
else:
    print("scalene triangle with sides", a, b, c)

#Program to find factorial of a number
n=5
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(factorial)
