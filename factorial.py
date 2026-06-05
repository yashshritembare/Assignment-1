num = int(input("enter your factorial number"))
 
fact = 1

for i in range(1,num + 1):
    fact=fact*i

print("factorial is",fact)