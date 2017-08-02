def DecToHex():
    result = int(input("Enter an integer: "))
    hexadecimal = ""
    while result != 0:
        remainder = alphabet(result % 16)
        hexadecimal = str(remainder) + hexadecimal
        result = int(result / 16)
    print(hexadecimal)

def alphabet(digit):
    decimal =     [10 , 11 , 12 , 13 , 14 , 15 ]
    hexadecimal = ["A", "B", "C", "D", "E", "F"]
    for counter in range(7):
        if digit == decimal[counter - 1]:
            digit = hexadecimal[counter - 1]
    return digit

DecToHex()
