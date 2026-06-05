
num = int(input("enter your number: "))
count = 0

while num > 0:
    count = count+1
    num = num // 10

print("Number of digit=", count)    