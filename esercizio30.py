lunghezza=int (input ("n. cifre del numero binario"))
totale=0
for n in range (lunghezza):
    cifra=int (input ("numero binario: "))
    valore=(cifra*2**n)
    totale+=valore
print(totale)