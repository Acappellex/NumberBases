octal = input('Enter an octal number: ')

decimal = 0

for digit in octal:
    decimal = decimal*8 + int(digit)

print (decimal)
