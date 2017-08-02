def DecToOct(n):
   if n > 1:
       DecToOct(n//8)
   print(n % 8, end = '')


integer = input("Enter an integer: ")

octal = int(integer)

DecToOct(octal)
