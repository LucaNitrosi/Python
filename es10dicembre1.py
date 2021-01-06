variabile1 = input("Inserisci una parola da verificare")
variabile2 = variabile1[::-1]
if variabile1 == variabile2:
    #doppio uguale segno di comparazione
   print ("La parola è palindroma")
else:
   print ("La parola non è palindroma")