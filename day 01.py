a= input("first number :")
b= input("second number :")
c= input("third number :")
d= input("fourth number :")

if (a > b and a > c and a > d):
    print("first number is the largest")
elif (b > c and b > d):
    print("second number is the largest")
elif ( c > d):
    print("third number is the largest")
else:
    print("fourth number is the largest")