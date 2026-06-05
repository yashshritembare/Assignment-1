
num1 = int(input("enter num1 value: "))
num2 = int(input("enter num2 value: "))
num3 = int(input("enter num3 value: "))

if num1>num2 and num1>num3:
    print("num1 is largest")
elif num2>num1 and num2>num3:
    print("num2 is largest")
else:
    print("num3 is largest")        