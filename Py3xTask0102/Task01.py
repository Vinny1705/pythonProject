#  = operator denotes assignment. Used to assign value to a variable
   #Examples : a=5, b-9.8

#   ==operator denotes equal to
   #Examples : a==9; b==9.8

# ** operator denotes raised to power
   #Examples : a**2, b**3

# ^ operator denotes XOR gate operation

#Program to find square and cube of a number
a=5
Square = a**2
Cube = a**3
print("Square is:",Square)
print("Cube is:",Cube)

#Program to find whether two numbers are equal to,less than or greater than

a=95
b=56
if a==b:
    print(a," is equal to", b)
elif a<b:
    print(a," is less than",b)
else:
    print(a,"is greater than", b)
