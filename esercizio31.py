a = int(input('n. intero da convertire in Binario \n'))
def decimalToBinary(n): 
     return bin(n).replace("0b","") 
if __name__ == '__main__': 
     print(decimalToBinary(a))  