def getdigit(digit):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    for x in range(len(digits)):
        if digit == digits[x]:
            return x

def HexToDec(hexa):
    dec = 0
    pwr = 0
    for digit in range(len(hexa), 0, -1):
        dec = dec + 16 ** pwr * getdigit(hexa[digit-1])
        pwr += 1
    print(str(dec))

hexadecimal = input("Enter an hexadecimal number: ")

HexToDec(hexadecimal)

