import math
while True:
    response=input('Enter Binary or decimal(B/D) or E for exit')
    if response.lower()=='b':
        binary=int(input("Enter the binary number"))
        decimal,power=0,0
        while binary!=0:
            rem=binary%10
            decimal=decimal+(rem*(2**power))
            power+=1
            binary=round(binary/10)
        print(decimal)
    elif response.lower()=='d':
        decimal=int(input("enter the decimal number"))
        binary=bin(decimal)
        print(binary[2:len(binary)])
    else:
        break
