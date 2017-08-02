def DecToBin(n):
   if n > 1:
       DecToBin(n//2)
   print(n % 2, end = '')


integer = input("Input your number: ")
dec = int(integer)
DecToBin(dec)
